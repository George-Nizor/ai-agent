import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    print("Hello from ai-agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=sys.argv[1]
        )
    except Exception as e:
        print(e)
        sys.exit(1)
    print(response.text)
    prompt_token_count = response.usage_metadata.prompt_token_count
    response_token_count = response.usage_metadata.candidates_token_count
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {response_token_count}")
    
if __name__ == "__main__":
    main()
