import gradio as gr
import os
from dotenv import load_dotenv
from interview_simulator import InterviewSimulator
import markdown
import json
from typing import Dict, List, Tuple

# Load environment variables
load_dotenv()

class InterviewWebInterface:
    def __init__(self):
        self.simulator = InterviewSimulator()
        self.current_conversation = []
        self.current_job_role = ""
        self.question_count = 0
        self.max_questions = 3
        self.interview_complete = False
        self.final_evaluation = ""

    def reset_interview(self) -> Tuple[str, str, str, str]:
        """Reset the interview state."""
        self.current_conversation = []
        self.current_job_role = ""
        self.question_count = 0
        self.interview_complete = False
        self.final_evaluation = ""
        return "", "", "Interview reset. Ready to start new interview.", gr.update(interactive=True)

    def format_conversation(self) -> str:
        """Format the conversation history for display."""
        if not self.current_conversation:
            return "No interview in progress."

        markdown_text = f"# Interview for {self.current_job_role} Position\n\n"
        
        for entry in self.current_conversation:
            markdown_text += f"### Question {self.current_conversation.index(entry) + 1}:\n"
            markdown_text += f"{entry['gpt_question']}\n\n"
            markdown_text += "#### Claude's Response:\n"
            markdown_text += f"{entry['claude_answer']}\n\n"
            markdown_text += "#### Gemini's Response:\n"
            markdown_text += f"{entry['gemini_answer']}\n\n"
            markdown_text += "---\n\n"

        if self.final_evaluation:
            markdown_text += "### Final Evaluation:\n"
            markdown_text += f"{self.final_evaluation}\n"

        return markdown_text

    def start_interview(self, job_role: str) -> Tuple[str, str, str, str]:
        """Start a new interview session."""
        if not job_role:
            return "", "", "Please enter a job role.", gr.update(interactive=True)

        self.current_job_role = job_role
        self.current_conversation = []
        self.question_count = 0
        self.interview_complete = False
        self.final_evaluation = ""

        # Get first question
        gpt_system, _, _ = self.simulator.create_system_prompts(job_role)
        first_question = self.simulator.call_gpt(self.current_conversation, gpt_system, is_first_question=True)
        
        return (
            first_question,
            "",
            f"Interview started for {job_role} position.",
            gr.update(interactive=False)
        )

    def process_responses(self, question: str) -> Tuple[str, str, str]:
        """Process the current question and get responses from both models."""
        if not question or self.interview_complete:
            return "", self.format_conversation(), "Please start a new interview."

        # Get responses from both models
        gpt_system, claude_system, gemini_system = self.simulator.create_system_prompts(self.current_job_role)
        claude_answer = self.simulator.call_claude(question, claude_system)
        gemini_answer = self.simulator.call_gemini(question, gemini_system)

        # Add to conversation history
        self.current_conversation.append({
            "gpt_question": question,
            "claude_answer": claude_answer,
            "gemini_answer": gemini_answer
        })

        self.question_count += 1

        # Check if interview is complete
        if self.question_count >= self.max_questions:
            self.interview_complete = True
            self.final_evaluation = self.simulator.call_gpt(
                self.current_conversation, 
                gpt_system, 
                is_final_evaluation=True
            )
            return "", self.format_conversation(), "Interview complete! See final evaluation above."

        # Get next question
        next_question = self.simulator.call_gpt(self.current_conversation, gpt_system)
        return next_question, self.format_conversation(), f"Question {self.question_count + 1} of {self.max_questions}"

    def create_interface(self) -> gr.Blocks:
        """Create the Gradio interface."""
        with gr.Blocks(title="AI Interview Simulator", theme=gr.themes.Soft()) as interface:
            gr.Markdown("""
            # AI Interview Simulator
            This system conducts technical interviews using multiple AI models:
            - GPT-4 as the interviewer
            - Claude and Gemini as candidates
            
            Enter a job role to begin the interview process.
            """)

            with gr.Row():
                with gr.Column(scale=1):
                    job_role_input = gr.Textbox(
                        label="Job Role",
                        placeholder="e.g., Senior Data Scientist",
                        lines=1
                    )
                    start_button = gr.Button("Start Interview")
                    reset_button = gr.Button("Reset Interview")

            with gr.Row():
                with gr.Column(scale=2):
                    current_question = gr.Textbox(
                        label="Current Question",
                        interactive=False,
                        lines=3
                    )
                    next_button = gr.Button("Get Responses & Next Question")
                    
            with gr.Row():
                with gr.Column(scale=2):
                    conversation_display = gr.Markdown(label="Interview Progress")
                    
            status_display = gr.Textbox(
                label="Status",
                interactive=False,
                lines=1
            )

            # Event handlers
            start_button.click(
                fn=self.start_interview,
                inputs=[job_role_input],
                outputs=[current_question, conversation_display, status_display, job_role_input]
            )

            next_button.click(
                fn=self.process_responses,
                inputs=[current_question],
                outputs=[current_question, conversation_display, status_display]
            )

            reset_button.click(
                fn=self.reset_interview,
                inputs=[],
                outputs=[current_question, conversation_display, status_display, job_role_input]
            )

        return interface

def main():
    """Main function to launch the web interface."""
    interface = InterviewWebInterface()
    app = interface.create_interface()
    app.launch(
        server_name="0.0.0.0",  # Makes the app accessible from other computers
        server_port=7860,       # Default Gradio port
        share=True             # Creates a public link
    )

if __name__ == "__main__":
    main()