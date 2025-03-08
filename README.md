# Multi-Model Interview Simulator

An advanced AI-powered interview simulation system that leverages multiple language models to create realistic technical interviews. The system uses GPT-4 as the interviewer while Claude and Gemini act as candidates, creating a unique and interactive interview experience.

## 🌟 Features

- **Multi-Model Integration**: Utilizes three powerful LLMs:
  - GPT-4 as the technical interviewer
  - Claude as candidate 1
  - Gemini as candidate 2

- **Dynamic Interview Process**:
  - Customizable job roles
  - Technical question generation based on role
  - Real-time candidate responses
  - Comprehensive evaluation system

- **Flexible Configuration**:
  - Adjustable number of interview questions
  - Customizable system prompts
  - Easy API key management

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
git clone https://github.com/yourusername/multi-model-interview-simulator.git
cd multi-model-interview-simulator
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
- Create a `.env` file in the root directory
- Add your API keys (see `.env.example` for format)

### Usage

1. Run the main script:
```bash
python interview_simulator.py
```

2. Enter the job role when prompted

3. Watch the interview unfold:
- GPT-4 will ask technical questions
- Claude and Gemini will provide responses
- Final evaluation will be provided

## 📁 Project Structure

```
multi-model-interview-simulator/
├── README.md
├── requirements.txt
├── .env.example
├── .env
├── src/
│   ├── __init__.py
│   ├── interview_simulator.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── gpt_interviewer.py
│   │   ├── claude_candidate.py
│   │   └── gemini_candidate.py
│   └── utils/
│       ├── __init__.py
│       └── prompt_manager.py
└── examples/
    └── sample_interview.ipynb
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following structure:
```env
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
```

### Customizing the Interview

You can modify:
- Number of questions
- System prompts
- Evaluation criteria
- Model parameters

See `config.py` for available options.

## 📝 Example Output

```
--- Starting Interview for Senior Data Scientist Position ---

Question 1: Can you explain the difference between L1 and L2 regularization and when you would use each?

Claude: [Technical response about regularization...]

Gemini: [Alternative perspective on regularization...]

[Interview continues...]

Final Evaluation:
[Detailed comparison and selection of candidate...]
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for GPT-4 API
- Anthropic for Claude API
- Google for Gemini API

## 📧 Contact

For questions and feedback, please open an issue or contact [your-email@example.com]