import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_readme(root_dir="."):
    allowed_extensions = {'.py', '.js', '.html', '.css', '.md', '.txt', '.json'}
    ignore_dirs = {'.git', '__pycache__', 'node_modules', '.venv', 'env'}
    
    context_text = "Project Directory Structure and Key File Contents:\n\n"
    
    for root, dirs, files in os.walk(root_dir):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        context_text += f"{indent}{os.path.basename(root)}/\n"
        
        for f in files:
            context_text += f"{indent}    - {f}\n"
            # Read small/medium files to give the AI context on what the code actually does
            if any(f.endswith(ext) for ext in allowed_extensions) and f != "README.md":
                try:
                    with open(os.path.join(root, f), 'r', encoding='utf-8') as code_file:
                        content = code_file.read()[:2000] # Limit per file to save tokens
                        context_text += f"{indent}        [Content of {f}]:\n{content}\n"
                except:
                    continue

    prompt = f"""
    Based on the following project structure and code snippets, generate a professional README.md.
    Include: Project Title, Description, Features, Installation (assume standard tools), and Usage.
    
    Project Data:
    {context_text}
    """

    print("--- Analyzing project and generating README ---")
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt
    )
    
    with open("GENERATED_README.md", "w") as out:
        out.write(response.text)
    print("Done! Check GENERATED_README.md")

if __name__ == "__main__":
    generate_readme()