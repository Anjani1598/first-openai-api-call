# First OpenAI API Call - Python Script

## 📜 Description

This script (`first_call.py`) demonstrates how to make a simple chat-based API call to OpenAI's `gpt-4o-mini` model using the OpenAI Python SDK. It takes a user prompt from the console, sends it to the assistant along with a fixed system prompt, and prints both the assistant’s reply and the total token usage.

---

## ⚙️ Requirements

- Python 3.7+
- `openai` SDK
- `python-dotenv` to manage API keys securely

---

## 📦 Installation & Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/first-openai-api-call.git
   cd first-openai-api-call
    ```
   
   2. **Create a virtual environment** (optional but recommended):
      ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      ```
3. **Install the required packages**:
   ```bash
   pip install openai python-dotenv
   ```
   
4. **Set up your OpenAI API key**:
    Create a `.env` file in the root directory of the project and add your OpenAI API key:
    ```plaintext
    OPENAI_API_KEY=sk-your-api-key-here
    ```
   
5. **Run the script**:
   6. ```bash
      python first_call.py
      ```


