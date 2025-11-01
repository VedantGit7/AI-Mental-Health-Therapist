# 🧠 AI Mental Health Therapist - معالج الصحة العقلية بالذكاء الاصطناعي

<div align="center">

**AI-Powered Mental Health Support System with Emergency Crisis Response**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-latest-green.svg)](https://github.com/langchain-ai/langchain)
[![LangGraph](https://img.shields.io/badge/LangGraph-latest-green.svg)](https://github.com/langchain-ai/langgraph)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-0078D4)](https://www.microsoft.com/windows)

[Features](#features) • [Demo Videos](#demo-videos) • [Quick Start](#quick-start) • [Architecture](#architecture) • [Contributing](#contributing)

</div>

---

## Overview

AI Mental Health Therapist is a **multilingual, empathetic mental health chatbot** powered by:
- **NVIDIA GPT-OSS-120B** (free, open-source LLM)
- **MedGemma** (medical/mental health optimized model via Ollama)
- **LangChain + LangGraph** (agentic AI framework)
- **Twilio** (emergency crisis response)

The system intelligently routes user queries through specialized tools to provide **therapeutic guidance, therapist connections, and emergency crisis intervention**—with support for **English, Arabic, and multilingual interactions**.

---

## Features

### 🎯 Core Capabilities

- **Empathetic Mental Health Support**: Therapeutic responses using MedGemma model with clinical psychology profiles
- **Emergency Crisis Detection**: Automatic detection of suicidal ideation and self-harm threats in multiple languages
- **Therapist Locator**: Find licensed therapists by location with contact information
- **Multilingual Support**: Seamlessly handle conversations in English, Arabic, Hindi, and more
- **24/7 Crisis Hotlines**: Integrated global emergency numbers with UAE, India, US, UK, and Australian helplines
- **Twilio Integration**: Automated emergency calls to safety hotlines when crisis detected

### 🛠️ Technical Highlights

- **Agentic AI**: Uses LangGraph's ReAct agent pattern for intelligent tool selection
- **Free LLM Integration**: NVIDIA GPT-OSS-120B API (no OpenAI subscription required)
- **Local Model Support**: Ollama integration for running MedGemma locally
- **Streaming Responses**: Real-time token streaming for responsive user experience
- **Context-Aware**: Maintains conversation history for coherent, personalized responses
- **Production-Ready**: Error handling, logging, and graceful degradation

---

## Demo Videos

### 🎬 English Demo
<video width="600" controls>
  <source src="https://github.com/VedantWedhaneGit/AI-Mental-Health-Therapist/tree/main/videos/english_conversation.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

https://github.com/VedantWedhaneGit/AI-Mental-Health-Therapist/tree/main/videos/english_conversation.mp4

**Features Demonstrated:**
- General anxiety/depression support
- Therapist search functionality
- Crisis response workflow

### 🎬 Arabic Demo
<video width="600" controls>
  <source src="https://github.com/VedantWedhaneGit/AI-Mental-Health-Therapist/tree/main/videos/arabic_conversation.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

https://github.com/VedantWedhaneGit/AI-Mental-Health-Therapist/tree/main/videos/arabic_conversation.mp4

**Features Demonstrated:**
- Multilingual support (Arabic)
- Emergency crisis detection
- UAE-specific hotline numbers
- Empathetic response generation

---

## Quick Start

### Prerequisites

- Python 3.10+
- `uv` package manager
- NVIDIA API key (free from [NVIDIA AI Foundation Models](https://build.nvidia.com/))
- Ollama installed with MedGemma model
- Twilio account (optional, for emergency calls)
- Windows/Mac/Linux

### Installation

1. **Clone the Repository**
git clone https://github.com/VedantWedhaneGit/AI-Mental-Health-Therapist.git
cd AI-Mental-Health-Therapist

2. **Create Virtual Environment**
uv init .

3. **Install Dependencies**
uv add langchain-openai langgraph python-dotenv twilio ollama

4. **Setup Environment Variables**
Edit `config.py` with your credentials:
NVIDIA API
NVIDIA_API_KEY=your_nvidia_api_key_here

Twilio (optional, for emergency calls)
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_FROM_NUMBER=your_twilio_number
EMERGENCY_CONTACT=+1234567890 

5. **Setup Ollama with MedGemma**
ollama pull alibayram/medgemma:4b

6. **Run the Agent**
uv run backend/ai_agent.py

---

## Architecture

### System Design

┌─────────────────────────────────────────────────────┐
│ User Input (Multi-language) │
└──────────────────────┬──────────────────────────────┘
│
┌──────────────────────▼──────────────────────────────┐
│ LangGraph ReAct Agent │
│ ┌─────────────────────────────────────────────┐ │
│ │ NVIDIA GPT-OSS-120B (LLM) │ │
│ │ - Temperature: 0.2 (consistent responses) │ │
│ │ - Max tokens: 4096 │ │
│ └─────────────────────────────────────────────┘ │
└──────────────────────┬──────────────────────────────┘
│
┌──────────────┼──────────────┐
│ │ │
┌───────▼────────┐ ┌──▼──────────┐ ┌─▼────────────────┐
│ MedGemma Tool │ │ Therapist │ │ Emergency Tool │
│ (via Ollama) │ │ Locator │ │ (Twilio + Crisis │
│ │ │ Tool │ │ Hotlines) │
│ Emotional │ │ │ │ │
│ Attunement │ │ Returns │ │ Detects suicide │
│ Normalization │ │ licensed │ │ Makes calls │
│ Guidance │ │ therapists │ │ Provides UAE/ │
│ Support │ │ by location │ │ Global numbers │
└────────────────┘ └─────────────┘ └──────────────────┘

### Tool Definitions

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| `ask_mental_health_specialist` | Therapeutic response | User query | Empathetic guidance |
| `find_nearby_therapists_by_location` | Find therapists | Location name | List of therapists |
| `emergency_call_tool` | Crisis response | None (auto-triggered) | Call confirmation + hotlines |

### Data Flow

1. **User Input**: Multilingual text input (Arabic, English, etc.)
2. **LLM Processing**: NVIDIA GPT-OSS-120B analyzes input and determines appropriate tool
3. **Tool Execution**: Selected tool processes the request
4. **Response Generation**: MedGemma or tool output returned to user
5. **Crisis Detection**: Suicidal ideation triggers emergency tool automatically

---

## Usage Examples

### Mental Health Support
User: "I'm feeling anxious and alone"
Agent: [Calls ask_mental_health_specialist]
Bot: "I understand how difficult this must be. Many people feel this way..."

### Find Therapist
User: "Can you help me find a therapist in Dubai?"
Agent: [Calls find_nearby_therapists_by_location]
Bot: "Of course! Here are therapists near Dubai..."

### Emergency Crisis Response
User: "I want to commit suicide" (Arabic or English)
Agent: [Calls emergency_call_tool]
Bot: "I'm placing an emergency call now. Please stay safe..."
[Shows UAE, India, US, UK, Australia hotlines]

---

## Configuration

### System Prompt Customization

Edit the `SYSTEM_PROMPT` in `ai_agent.py` to adjust:
- Therapist personality profile
- Tool selection priorities
- Crisis detection sensitivity
- Response tone and language

### Temperature Tuning

- **Current**: 0.2 (deterministic, therapeutic consistency)
- **Adjustment**: 0.3-0.5 for more varied responses
- Modify in `ai_agent.py`: `temperature=0.2`

### Model Parameters

llm = ChatOpenAI(
api_key=NVIDIA_API_KEY,
base_url=NVIDIA_BASE_URL,
model="openai/gpt-oss-120b",
temperature=0.2, # Adjust for creativity vs. consistency
max_tokens=4096, # Maximum response length
streaming=True # Enable real-time token streaming
)

---

## Project Structure

safespace-ai-agent/
├── backend/
│ ├── ai_agent.py # Main agent logic with tools
│ ├── tools.py # Tool implementations (MedGemma, Twilio, Therapist)
│ ├── config.py # Environment configuration
│ └── init.py
├── docs/
│ ├── ARCHITECTURE.md # Detailed system architecture
│ ├── API_REFERENCE.md # Tool API documentation
│ └── SETUP_GUIDE.md # Extended setup instructions
├── videos/
│ ├── demo_english.mp4 # English demo (General support)
│ └── demo_arabic.mp4 # Arabic demo (Crisis response)
├── tests/
│ ├── test_mental_health_specialist.py
│ └── test_emergency_tool.py
├── .env.example # Environment variables template
├── .gitignore # Git ignore rules
├── pyproject.toml # Project metadata and dependencies
├── uv.lock # Dependency lock file
└── README.md # This file


---

## Installation & Development

### For Ubuntu/Linux/Mac:
git clone https://github.com/VedantWedhaneGit/AI-Mental-Health-Therapist.git
cd AI-Mental-Health-Therapist
uv venv
source .venv/bin/activate
uv add -r requirements.txt
ollama pull alibayram/medgemma:4b
uv run backend/ai_agent.py

### For Windows:
git clone https://github.com/VedantWedhaneGit/AI-Mental-Health-Therapist.git
cd AI-Mental-Health-Therapist
uv venv
.venv\Scripts\activate
uv add langchain-openai langgraph python-dotenv twilio ollama
ollama pull alibayram/medgemma:4b
uv run backend/ai_agent.py


---

## Testing

### Test Scenarios Included

1. **General Mental Health**: Anxiety and depression support
2. **Therapist Search**: Locate professionals by location
3. **Crisis Detection**: Suicidal ideation (Arabic & English)
4. **Panic Attack**: Real-time anxiety management
5. **Recovery Guidance**: Post-crisis follow-up

### Run Tests
uv run pytest tests/

### Manual Testing

Use the test chat scenarios in `docs/TEST_SCENARIOS.md`:
- Scenario 1: General mental health concern
- Scenario 2: Seeking therapist
- Scenario 3: Emergency crisis (Arabic)
- Scenario 4: Recovery follow-up
- Scenario 5: Panic attack management

---

## System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Python | 3.10 | 3.11+ |
| RAM | 8 GB | 16 GB |
| GPU | CPU only | NVIDIA GPU (optional) |
| Storage | 2 GB | 5 GB (with models) |
| Internet | Required | Required |

**Tested Environment:**
- OS: Windows 11 / Ubuntu 20.04+
- CPU: Intel i7-7th Gen or newer
- GPU: NVIDIA GTX 1050 (optional)
- RAM: 16 GB

---

## Technologies Used

### Core Framework
- **LangChain**: LLM orchestration and tool management
- **LangGraph**: Agentic AI with graph-based workflows
- **NVIDIA GPT-OSS-120B**: Free, open-source language model

### NLP & Models
- **MedGemma (via Ollama)**: Medical/mental health specialized model
- **Ollama**: Local model runtime and management

### Communication & APIs
- **OpenAI API (compatible)**: NVIDIA endpoint integration
- **Twilio**: Emergency calling and SMS capabilities
- **Python-dotenv**: Secure environment configuration

### Development
- **uv**: Fast Python package manager
- **Python 3.10+**: Modern Python features
- **Git**: Version control

---

## API Keys & Setup

### 1. NVIDIA API Key (Free)
1. Go to [NVIDIA AI Foundation Models](https://build.nvidia.com/)
2. Sign up for free account
3. Navigate to "API Keys" section
4. Copy your key to `.env`:
NVIDIA_API_KEY=nvapi-xxxxxxxxxxxxx


### 2. Ollama Setup (Free)
1. Download from [ollama.ai](https://ollama.ai)
2. Install and run: `ollama serve`
3. In another terminal: `ollama pull alibayram/medgemma:4b`

### 3. Twilio Setup (Optional, for emergency calls)
1. Create account at [twilio.com](https://twilio.com)
2. Get phone number, account SID, and auth token
3. Add to `.env`:
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_token_here
TWILIO_FROM_NUMBER=+1234567890
EMERGENCY_CONTACT=+your_emergency_number

---

## Features in Action

### ✅ Implemented
- [x] Multilingual support (Arabic, English, Hindi)
- [x] Crisis detection and emergency response
- [x] Therapist locator by location
- [x] Empathetic MedGemma integration
- [x] Twilio emergency calling
- [x] Global crisis hotlines (UAE, India, US, UK, Australia)
- [x] Streaming responses
- [x] Error handling and graceful degradation

### 🔄 Future Enhancements
- [ ] Database integration for therapist management
- [ ] User authentication and session management
- [ ] Frontend web/mobile UI
- [ ] Advanced NLP for condition classification
- [ ] Integration with mental health platforms
- [ ] Multi-user support and analytics
- [ ] Sentiment analysis and mood tracking
- [ ] Appointment scheduling system

---

## Performance & System Specs

**Tested on Intel i7-7th Gen (16GB RAM, GTX 1050)**

| Metric | Value |
|--------|-------|
| Average Response Time | 2-5 seconds |
| Model Load Time | ~3-5 seconds |
| Memory Usage | ~4-6 GB |
| GPU Usage | Optional (1-2 GB if used) |
| Max Concurrent Users | 1 (local) |

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8
- Use type hints for all functions
- Document all public methods with docstrings
- Include unit tests for new features

---

## Troubleshooting

### Issue: `ImportError: cannot import name 'tool' from 'langchain.agents'`
**Solution**: Import from `langchain_core.tools` instead:
from langchain_core.tools import tool

### Issue: MedGemma Model Not Found
**Solution**: Pull the model first:
ollama pull alibayram/medgemma:4b

### Issue: NVIDIA API Authentication Failed
**Solution**: Verify your API key in `.env` and ensure you have API access enabled.

### Issue: Twilio Call Not Working
**Solution**: Check Twilio credentials, ensure phone numbers are in E.164 format (+1234567890).

For more troubleshooting, see [SETUP_GUIDE.md](docs/SETUP_GUIDE.md).

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## Citation & References

If you use AI-Mental-Health-Therapist in your research or projects, please cite:
@software{AI-Mental-Health-Therapist,
author = {Vedant Wedhane},
title = {AI-Mental-Health-Therapist: AI-Powered Mental Health Support System},
year = {2025},
url = {https://github.com/VedantWedhaneGit/AI-Mental-Health-Therapist.git}
}

### Key References
- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Guide](https://langchain-ai.github.io/langgraph/)
- [NVIDIA AI Foundation Models](https://build.nvidia.com/)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [Twilio Python Documentation](https://www.twilio.com/docs/python)

---

## Support & Contact

For questions, issues, or suggestions:
- 📧 Email: vedantwedhane@gmail.com
- 🐙 GitHub Issues: [Open an Issue](https://github.com/VedantWedhaneGit/AI-Mental-Health-Therapist.git/issues)
- 💬 Discussions: [Start a Discussion](https://github.com/VedantWedhaneGit/AI-Mental-Health-Therapist.git/discussions)

### Emergency Resources
If you or someone you know is in crisis:
- **India**: 9152987821 (Samaritans) or 1098 (National Helpline)
- **UAE**: 800 4673 (HOPE) or 800 111 (Dubai)
- **USA**: 988 (Suicide & Crisis Lifeline)
- **UK**: 116 123 (Samaritans)
- **Australia**: 13 11 14 (Lifeline)

---

<div align="center">

**Made with ❤️ for mental health support**

⭐ If this project helped you, please consider giving it a star!

</div>

