# Enhanced LLM Chatbot

An advanced chatbot system using Llama 2 with context-aware responses, sentiment analysis, and quick replies.

## Project Structure
```
enhanced-llm-chatbot/
├── src/
│   ├── models/
│   │   ├── nlp_engine.py
│   │   └── llm_client.py
│   ├── services/
│   │   ├── conversation_manager.py
│   │   └── llm_service.py
│   └── main.py
├── tests/
├── Dockerfile
└── requirements.txt
```

## Features
- Llama 2 integration with 4-bit quantization
- Context-aware response generation
- Sentiment analysis and entity recognition
- Quick replies based on context
- Analytics and feedback mechanisms

## Setup Instructions
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python src/main.py`

## Documentation
Full documentation available in the /docs folder.

## License
MIT License