import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    # Greeting
    print("Hello from ai-agent!")
    
    # Initialise Client and Environment Variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    # Parse Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="The prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    user_prompt = args.prompt

    # Create Messages
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    # Send Request
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages
        )
    except Exception as e:
        print(e)
        sys.exit(1)
    print(response.text)
    if args.verbose:
        prompt_token_count = response.usage_metadata.prompt_token_count
        response_token_count = response.usage_metadata.candidates_token_count
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_token_count}")
        print(f"Response tokens: {response_token_count}")
    
if __name__ == "__main__":
    main()
