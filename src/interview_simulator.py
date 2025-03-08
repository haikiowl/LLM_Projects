import os
from dotenv import load_dotenv
from openai import OpenAI
import anthropic
from typing import List, Dict, Tuple

# Load environment variables
load_dotenv()

class InterviewSimulator:
    def __init__(self):
        # Initialize API clients
        self.openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.gemini_client = OpenAI(
            api_key=os.getenv("GOOGLE_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        
        # Load model configurations
        self.gpt_model = os.getenv("GPT_MODEL", "gpt-4")
        self.claude_model = os.getenv("CLAUDE_MODEL", "claude-3-haiku-20240307")
        self.gemini_model = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
        
        # Load interview settings
        self.max_tokens = int(os.getenv("MAX_RESPONSE_TOKENS", "300"))
    
    def create_system_prompts(self, job_role: str) -> Tuple[str, str, str]:
        """Create system prompts for all models based on job role."""
        gpt_prompt = f"""You are an interviewer conducting a technical job interview for a {job_role} position.
Your task is to ask 3 precise, technical questions that are directly relevant to the {job_role} role.
Ask one question at a time. Keep your questions concise and focused."""

        candidate_prompt = f"""You are a candidate in a job interview for a {job_role} position.
Answer the interviewer's questions thoughtfully and professionally.
Keep your answers concise and under 200 words.
Focus on technical accuracy and practical experience."""

        return gpt_prompt, candidate_prompt, candidate_prompt

    def call_gpt(self, conversation_history: List[Dict], gpt_system: str, 
                is_final_evaluation: bool = False, is_first_question: bool = False) -> str:
        """Generate interviewer questions or evaluation using GPT."""
        messages = [{"role": "system", "content": gpt_system}]
        
        # Add conversation history
        for entry in conversation_history:
            if "gpt_question" in entry:
                messages.append({"role": "assistant", "content": entry["gpt_question"]})
            if "claude_answer" in entry:
                messages.append({"role": "user", "content": f"Claude's answer: {entry['claude_answer']}"})
            if "gemini_answer" in entry:
                messages.append({"role": "user", "content": f"Gemini's answer: {entry['gemini_answer']}"})

        # Add appropriate instruction based on context
        if is_final_evaluation:
            messages.append({
                "role": "user", 
                "content": "Please evaluate both candidates based on all their answers and select one for the position. Provide your reasoning."
            })
        elif is_first_question:
            messages.append({
                "role": "user", 
                "content": "Please ask your first technical question for this role. Make it precise and directly relevant to the role."
            })
        else:
            messages.append({
                "role": "user", 
                "content": "Based on these responses, please ask your next precise technical question for this role."
            })

        try:
            completion = self.openai.chat.completions.create(
                model=self.gpt_model,
                messages=messages
            )
            return completion.choices[0].message.content
        except Exception as e:
            print(f"Error calling GPT: {e}")
            return "Could not generate question. Please try again."

    def call_claude(self, question: str, claude_system: str) -> str:
        """Get response from Claude as a candidate."""
        try:
            message = self.claude.messages.create(
                model=self.claude_model,
                system=claude_system,
                messages=[
                    {"role": "user", "content": f"Interviewer's question: {question}. Remember to keep your answer under 200 words."}
                ],
                max_tokens=self.max_tokens
            )
            return message.content[0].text
        except Exception as e:
            print(f"Error calling Claude: {e}")
            return "Claude could not generate a response. Please try again."

    def call_gemini(self, question: str, gemini_system: str) -> str:
        """Get response from Gemini as a candidate."""
        try:
            response = self.gemini_client.chat.completions.create(
                model=self.gemini_model,
                messages=[
                    {"role": "system", "content": gemini_system},
                    {"role": "user", "content": f"Interviewer's question: {question}. Remember to keep your answer under 200 words."}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error calling Gemini: {e}")
            return "Gemini could not generate a response. Please try again."

    def conduct_interview(self, job_role: str, num_questions: int = 3) -> Tuple[List[Dict], str]:
        """Conduct the complete interview process."""
        conversation_history = []
        gpt_system, claude_system, gemini_system = self.create_system_prompts(job_role)
        
        print(f"\n--- Starting Interview for {job_role} Position ---\n")
        
        # Initial question from GPT
        initial_question = self.call_gpt(conversation_history, gpt_system, is_first_question=True)
        
        for i in range(num_questions):
            # Get the current question from GPT
            current_question = initial_question if i == 0 else self.call_gpt(conversation_history, gpt_system)
            
            # Add question to history
            conversation_history.append({"gpt_question": current_question})
            
            # Get responses from both models
            claude_answer = self.call_claude(current_question, claude_system)
            gemini_answer = self.call_gemini(current_question, gemini_system)
            
            # Add responses to history
            conversation_history[-1]["claude_answer"] = claude_answer
            conversation_history[-1]["gemini_answer"] = gemini_answer
            
            print(f"\nQuestion {i+1}: {current_question}")
            print(f"\nClaude: {claude_answer}")
            print(f"\nGemini: {gemini_answer}")
            print("\n" + "-"*50 + "\n")
        
        # Final evaluation
        final_evaluation = self.call_gpt(conversation_history, gpt_system, is_final_evaluation=True)
        print("\nFinal Evaluation:")
        print(final_evaluation)
        
        return conversation_history, final_evaluation

def main():
    """Main function to run the interview simulator."""
    simulator = InterviewSimulator()
    
    # Get job role from user
    job_role = input("Enter the job role for the interview: ")
    num_questions = int(os.getenv("DEFAULT_NUM_QUESTIONS", "3"))
    
    print(f"\nStarting LLM Interview for {job_role} position with GPT as interviewer, Claude and Gemini as candidates...")
    conversation, evaluation = simulator.conduct_interview(job_role, num_questions)
    print("\nInterview complete!")

if __name__ == "__main__":
    main()