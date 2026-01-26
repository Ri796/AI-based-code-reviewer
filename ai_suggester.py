from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Ensure API Token is available
sec_key = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = sec_key

def get_code_suggestions(code_string):
    """
    Analyzes the provided code using ChatHuggingFace and Zephyr/Qwen model.
    Returns a string response compatible with the UI.
    """
    if not sec_key:
        return "❌ Error: Missing Hugging Face API Token. Please add 'HF_TOKEN' to your .env file."

    try:
        # Using Zephyr-7b-beta
        llm = HuggingFaceEndpoint(
            repo_id='HuggingFaceH4/zephyr-7b-beta',
            temperature=0.3, # Low temperature for deterministic results
            max_new_tokens=4096,
            repetition_penalty=1.1, # Prevent looping
            top_k=50,
            top_p=0.95
        )

        model = ChatHuggingFace(llm=llm)

        system_prompt = """You are an expert Python Code Reviewer.
Your task is to analyze the code and output a report in the EXACT format below.
IMPORTANT: Ensure the 'Improved Code' block is strictly closed with triple backticks (```) BEFORE starting the 'Detailed Explanations' section.
IMPORTANT: Do NOT rename variables unless strictly necessary for correctness. Preserve original variable names (like 'i', 'x', 'count') to keep the diff clean. Avoid stylistic changes that do not fix bugs.
IMPORTANT: Provide ONLY the single best improved version of the code. Do NOT provide multiple options, "Alternative 1", or "Case A/B". Just give the one optimal solution.

### Output Template:
# AI Code Analysis Report
Date: {date}
Quality Grade: [A/B/C/D/F]
Issues Found: [Count]

## Review Findings
## Analysis Summary
[Brief summary of the code and its status]

## Issues Found
- Issue: [Description of issue 1]
- Issue: [Description of issue 2]

## Improved Code
```python
[The complete, fixed code. Include ALL necessary imports. Fix all bugs and unused imports.]
```

## Detailed Explanations

### 🚀 Scalability Impact
- **Scalability**: [Analysis]
- **Performance**: [Analysis]
- **Memory Usage**: [Analysis]
- **Resource Management**: [Analysis]

### ⏱️ Time/Space Complexity
- **Algorithm Efficiency**: [O(n), etc.]
- **Big O Notation**: [Explanation]
- **Memory Allocation**: [Analysis]
- **Computational Cost**: [Analysis]

### 📖 Readability & Maintainability
- **Code Clarity**: [Analysis]
- **Documentation Benefits**: [Analysis]
- **Team Collaboration**: [Analysis]
- **Future Maintenance**: [Analysis]

### 📋 Best Practices & PEP8
- **Python Coding Standards Compliance**: [Analysis]
- **Industry Best Practices**: [Analysis]
"""
        
        # Inject date dynamically is hard in prompt, so AI will guess or we just let it put a placeholder. 
        # Actually letting AI put the date is fine.
        
        user_prompt = f"Review this Python code:\n{code_string}"

        response = model.invoke(
            [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_prompt)
            ]
        )
        
        return response.content
        
    except Exception as e:
        error_msg = str(e)
        if "401" in error_msg:
             return f"❌ **Auth Error**: Invalid Token. Check your .env file.\nRef: {error_msg}"
        elif "429" in error_msg:
             return f"❌ **Rate Limit**: API Busy. Try again in 1 minute.\nRef: {error_msg}"
        else:
            return f"❌ **Error**: {error_msg}"


def ask_code_question(code, question):
    """
    Asks a question about the code.
    """
    try:
        llm = HuggingFaceEndpoint(
            repo_id='HuggingFaceH4/zephyr-7b-beta',
            temperature=0.3
        )
        model = ChatHuggingFace(llm=llm)

        response = model.invoke([
            SystemMessage(content="You are a helpful coding assistant. Answer questions specifically about the provided code snippet."),
            HumanMessage(content=f"Code:\n{code}\n\nQuestion: {question}")
        ])
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"
