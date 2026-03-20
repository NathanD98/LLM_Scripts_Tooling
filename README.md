# LLM Document Review and Summarization

This Python script automatically reviews and summarizes documents using the Google Gemini API. It takes a document file as input and generates a concise bullet-point summary leveraging the Gemini 2.0 Flash model.

## Features

*   **Automated Summarization:** Quickly summarizes documents with Gemini.
*   **Easy Setup:** Simple script execution.
*   **Clear Output:** Provides the generated summary.
*   **Workflow Visualization:** Illustrated with a Mermaid workflow graph.

## Prerequisites

*   **Python 3.7+:** Ensure you have Python 3.7 or higher installed on your system.
*   **Google Gemini API Key:** You’ll need a valid Google Gemini API key to use this script. See the instructions below for setting it up.
*   **Mermaid:**  Make sure you have a Mermaid editor or viewer to render the workflow graph (e.g., [Mermaid Live Editor](https://mermaid.live/).)

## Setting Up Your Google Gemini API Key

1.  **Create a Google Cloud Project:** If you don’t already have one, create a new Google Cloud project.  Go to [https://console.cloud.google.com/](https://console.cloud.google.com/) and follow the instructions.
2.  **Enable the Gemini API:** In your Google Cloud project, search for "Gemini API" and enable it.
3.  **Create an API Key:** Go to "Credentials" and click "+ CREATE CREDENTIALS" > "API Key".  A new API key will be generated.
4.  **Set the API Key:**  Modify the `LLM-review-docs.py` script to set your API key:

    ```python
    # Replace with your actual API key
    # 1. Load environment variables
      api_key = os.getenv("GOOGLE_API_KEY")
    ```

## Workflow Diagram

This section includes a Mermaid diagram illustrating the script's workflow.  You can copy and paste this code into a Mermaid editor to visualize it.

```mermaid
graph LR
    A[Start] --> B{Input Document};
    B --> C{Call Gemini API};
    C --> D{Receive Summary};
    D --> E[Output Summary];
    E --> F[End];
