import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="OpenAI Text Generation API", version="1.0.0")

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

client = OpenAI(api_key=api_key)


# Pydantic models for request/response
class TextGenerationRequest(BaseModel):
    prompt: str
    model: str = "gpt-3.5-turbo"
    max_tokens: int = 150


class TextGenerationResponse(BaseModel):
    generated_text: str
    model_used: str
    prompt: str


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "OpenAI Text Generation API is running!"}


@app.post("/generate", response_model=TextGenerationResponse)
async def generate_text(request: TextGenerationRequest):
    """Generate text using OpenAI API"""
    try:
        response = client.chat.completions.create(
            model=request.model,
            messages=[{"role": "user", "content": request.prompt}],
            max_tokens=request.max_tokens,
        )

        generated_text = response.choices[0].message.content

        return TextGenerationResponse(
            generated_text=generated_text,
            model_used=request.model,
            prompt=request.prompt,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating text: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "OpenAI Text Generation API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
