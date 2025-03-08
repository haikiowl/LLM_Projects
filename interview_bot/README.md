# Multi-Model Interview Simulator

An advanced AI-powered interview simulation system that leverages multiple language models to create realistic technical interviews. The system uses GPT-4 as the interviewer while Claude and Gemini act as candidates.

## 🌟 Features

- **Multi-Model Integration**:
  - GPT-4 as the technical interviewer
  - Claude as candidate 1
  - Gemini as candidate 2

- **Web Interface**:
  - User-friendly Gradio interface
  - Real-time interview progress
  - Interactive question-answer flow
  - Markdown-formatted conversation display

- **Dynamic Interview Process**:
  - Customizable job roles
  - Technical question generation
  - Real-time candidate responses
  - Comprehensive evaluation system

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- API keys for:
  - OpenAI (GPT-4)
  - Anthropic (Claude)
  - Google (Gemini)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/LLM_Projects.git
cd LLM_Projects/interview_bot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
- Copy `.env.example` to `.env`
- Add your API keys

### Usage

#### Web Interface

1. Start the web interface:
```bash
python src/web_interface.py
```

2. Open your browser and navigate to:
- Local: http://localhost:7860
- Public: Check the console for the public URL

3. Using the interface:
   - Enter the job role
   - Click "Start Interview"
   - Watch the interview progress
   - Use "Get Responses & Next Question" to advance
   - View the final evaluation at the end

#### Command Line Interface

1. Run the CLI version:
```bash
python src/interview_simulator.py
```

2. Follow the prompts to:
   - Enter job role
   - View questions and responses
   - Get final evaluation

## 🖥️ Web Interface Features

### Main Components

1. **Job Role Input**:
   - Enter any technical job role
   - Examples: "Senior Data Scientist", "Full Stack Developer"

2. **Interview Control**:
   - Start Interview: Begin a new session
   - Reset Interview: Clear current progress
   - Get Responses: Proceed to next question

3. **Display Areas**:
   - Current Question: Shows active question
   - Interview Progress: Full conversation history
   - Status: Current state and instructions

### Interview Flow

1. **Starting an Interview**:
   - Enter job role
   - Click "Start Interview"
   - First question appears automatically

2. **During Interview**:
   - View current question
   - Click "Get Responses" to see candidates' answers
   - Next question appears automatically
   - Progress shown in markdown format

3. **Completion**:
   - Final evaluation shown after last question
   - Option to reset and start new interview

## 📝 Example Output

```markdown
# Interview for Senior Data Scientist Position

### Question 1:
Can you explain the difference between L1 and L2 regularization?

#### Claude's Response:
[Technical response about regularization...]

#### Gemini's Response:
[Alternative perspective on regularization...]

[Interview continues...]

### Final Evaluation:
[Detailed comparison and selection of candidate...]
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For questions and feedback, please open an issue or contact [your-email@example.com]