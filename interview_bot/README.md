# Multi-Model Interview Simulator

An advanced AI-powered interview simulation system that leverages multiple language models to create realistic technical interviews. The system uses GPT-4 as the interviewer while Claude and Gemini act as candidates.

## 🌟 Features

- **Multi-Model Integration**:
  - GPT-4 as the technical interviewer
  - Claude as candidate 1
  - Gemini as candidate 2

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

#### Command Line Interface

1. Run the CLI version:
```bash
python src/interview_simulator.py
```

2. Follow the prompts to:
   - Enter job role
   - View questions and responses
   - Get final evaluation

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