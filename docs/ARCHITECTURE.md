# System Architecture

## High-Level Overview

SafeSpace AI Agent uses a **ReAct (Reasoning + Acting) pattern** with LangGraph to create an agentic system that can:

1. **Reason**: Analyze user input to determine appropriate response
2. **Act**: Execute specialized tools based on the analysis
3. **Respond**: Generate empathetic, context-aware responses

## Component Architecture

### 1. Input Layer
- Accepts multilingual text (English, Arabic, Hindi, etc.)
- No preprocessing required

### 2. LLM Layer (NVIDIA GPT-OSS-120B)
- Processes input and determines which tool to use
- Temperature: 0.2 (deterministic, consistent)
- Streaming enabled for real-time responses

### 3. Tool Layer

#### Tool 1: Mental Health Specialist
- Uses MedGemma (medical LLM)
- Provides therapeutic responses
- System prompt: Clinical psychologist personality
- Parameters: 350 token limit, temperature 0.7

#### Tool 2: Therapist Locator
- Finds licensed therapists by location
- Can be extended to real database

#### Tool 3: Emergency Call Tool
- Detects crisis situations
- Triggers Twilio emergency calls
- Provides multi-language hotlines

### 4. Output Layer
- Streaming responses to user
- Crisis hotline numbers when needed
- Therapist contact information

## Data Flow Diagram

User Input (Arabic/English/etc)
↓
LangGraph Agent
(NVIDIA GPT-OSS-120B)
↓
Tool Selection Logic
↙ ↓ ↘
Tool1 Tool2 Tool3
(MedGemma) (Locate) (Emergency)
↘ ↓ ↙
Response Generation
↓
User Output + Hotlines

## Tool Decision Logic

IF user_input contains crisis keywords (suicide, self-harm):
→ Call emergency_call_tool()
ELIF user_input asks about therapists:
→ Call find_nearby_therapists_by_location()
ELSE:
→ Call ask_mental_health_specialist()

## Integration Points

### External APIs
- **NVIDIA GPT-OSS-120B**: Primary LLM via OpenAI-compatible endpoint
- **Ollama**: Local MedGemma model runtime
- **Twilio**: Emergency calling service

### Configuration
- Environment variables in `.env`
- System prompts in `ai_agent.py`
- Tool parameters in `tools.py`

## Performance Characteristics

- **Latency**: 2-5 seconds per response
- **Memory**: 4-6 GB for full system
- **Scalability**: Single-user (local), can be extended with Flask/FastAPI

## Security Considerations

- API keys stored in `.env` (never committed to git)
- `.gitignore` protects sensitive files
- Twilio credentials isolated in config
- No user data persistence (stateless)
