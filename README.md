# OpenAI API Integration Solutions

This project demonstrates how to integrate and use the OpenAI API for text generation.

## Setup Instructions

### 1. Install Dependencies

First, install the required Python packages:

```bash
pip install -r rqeuirements.txt
```

### 2. Configure API Key

#### Option A: Using .env file (Recommended)

1. Copy the template file:
   ```bash
   cp .env.template .env
   ```

2. Edit the `.env` file and replace `your_api_key_here` with your actual OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

3. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

#### Option B: Using Environment Variables

Set the environment variable directly in your terminal:

```bash
export OPENAI_API_KEY="sk-your-actual-api-key-here"
```

### 3. Run the Application

#### Option A: Console Application
```bash
cd text-gen
python main.py
```

#### Option B: Web API with Uvicorn
```bash
cd text-gen
python app.py
```

Or run with uvicorn directly:
```bash
cd text-gen
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:
- Main endpoint: http://localhost:8000
- API documentation: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

#### Example API Usage:
```bash
curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "What is the capital of India?", "model": "gpt-3.5-turbo"}'
```

## About Uvicorn

Uvicorn is an ASGI server (not a package manager) that runs modern Python web applications. It's particularly popular with FastAPI applications because it provides:

- High performance asynchronous request handling
- WebSocket support
- HTTP/2 support
- Auto-reloading during development
- Production-ready deployment capabilities

## Security Notes

- Never commit your actual API key to version control
- The `.env` file is already ignored by git
- Always use environment variables for sensitive data
- Consider using different API keys for development and production

## Project Structure

```
├── README.md
├── rqeuirements.txt
├── .env.template
├── .gitignore
└── text-gen/
    ├── main.py          # Console application
    └── app.py           # FastAPI web application
```

## Dependencies Added

- **openai**: OpenAI Python client library
- **python-dotenv**: Load environment variables from .env files
- **fastapi**: Modern web framework for building APIs
- **uvicorn[standard]**: ASGI server for running FastAPI applications
