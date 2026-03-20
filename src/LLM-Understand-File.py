import os
import sys

# 1. Load environment variables
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("ERROR: GOOGLE_API_KEY not found in environment.")
    sys.exit(1)

try:
    from google import genai
except ImportError:
    print("ERROR: 'google-genai' not found. Run: pip install google-genai")
    sys.exit(1)

# 2. Initialize Client
client = genai.Client(api_key=api_key)

class DocumentConverter:
    def convert(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            result = type('Result', (object,), {'document': content})()  # Corrected line
            return result
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

def summarize_document(file_path):
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found."

    try:
        print(f"--- Parsing Document: {file_path} ---")
        converter = DocumentConverter()
        result = converter.convert(file_path)
        if result is None:
            return "Error: Document conversion failed."
        content = result.document
        
        # Check if content is empty
        if not content.strip():
            return "Error: Document appears to be empty or unreadable."

        print("--- Generating Summary ---")
        # 3. Using System Instructions for better control
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            config={
                "system_instruction": "You are a professional editor. Provide a concise, high-level summary of the provided document using bullet points."
            },
            contents=content
        )
        
        return response.text

    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    target = "tester.md"
    print(summarize_document(target))
