import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key  = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    parser = argparse.ArgumentParser(description="Generate content using Gemini API")
    parser.add_argument('prompt', type=str, help='The prompt to generate content for')
    parser.add_argument("--verbose", "-v", action="store_true", help="Increase output verbosity")
    args = parser.parse_args()
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=args.prompt)])
    ]  
          
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    print(response.text)
    if args.verbose:
        print("User prompt: " + args.prompt)
        print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(response.usage_metadata.thoughts_token_count))
    sys.exit(0)

if __name__ == "__main__":
    main()
