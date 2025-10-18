import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def generate_text():
    # Get API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        print("Please set your API key in the .env file or as an environment variable")
        return

    client = OpenAI(api_key=api_key)
    text_response = None
    try:
        # Fixed API call - using chat completions instead of responses
        text_response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use a valid model
            messages=[{"role": "user", "content": "What is the capital of India?"}],
        )
    except Exception as e:
        print(f"Error occurred: {e}")
    else:
        # Extract the response text correctly
        print(text_response.choices[0].message.content)
    print(f"The generated response: {text_response}")


if __name__ == "__main__":
    generate_text()
