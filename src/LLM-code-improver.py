import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def review_code(file_path):
    if not os.path.exists(file_path):
        return "File not found."

    with open(file_path, 'r', encoding='utf-8') as f:
        code_content = f.read()

    # System instruction sets the "persona" of the AI
    sys_instr = (
        "You are a Senior Software Engineer. Review the provided code for: "
        "1. Logical bugs. 2. Security vulnerabilities. 3. Readability/PEP8 issues. "
        "Provide your feedback in a structured format with 'Issue', 'Suggested Fix', and 'Why'."
    )

    print(f"--- Auditing: {file_path} ---")
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        config={"system_instruction": sys_instr},
        contents=f"Please review this code:\n\n{code_content}"
    )
    
    return response.text

if __name__ == "__main__":
    # Point this at any file you want reviewed
    report = review_code("target_script.py") 
    print(report)