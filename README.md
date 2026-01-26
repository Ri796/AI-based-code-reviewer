# AI Code Reviewer

An advanced AI-powered code auditing tool that helps developers write clean, efficient, and secure Python code.

## Features
- **AI-Powered Analysis**: Uses `HuggingFaceH4/zephyr-7b-beta` to provide deep insights on bugs, security, and performance.
- **Static Analysis**: Detects syntax errors and unused variables using Python's AST.
- **Auto-Formatting**: Automatically formats code to PEP 8 standards using `autopep8`.
- **History Tracking**: Keeps a session-based history of your analyses.
- **Q&A Assistant**: Ask questions about your code directly to the AI.
- **Rich UI**: A dark-themed, responsive interface with sidebar navigation.

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**
   Create a `.env` file in the project root and add your Hugging Face API Token:
   ```
   HF_TOKEN=your_token_here
   ```
   *Note: You can get a free token from [Hugging Face Settings](https://huggingface.co/settings/tokens).*

3. **Run the Application**
   ```bash
   streamlit run main.py
   ```

## Built With
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Hugging Face](https://huggingface.co/)
