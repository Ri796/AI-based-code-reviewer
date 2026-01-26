import streamlit as st
from ui import setup_page, render_sidebar, render_code_studio, render_insights_report, render_history

# Page Config (Must be the first Streamlit command)
st.set_page_config(page_title="AI Code Reviewer", layout="wide", page_icon="�")

# Initialize Session State logic for history if needed
if "history" not in st.session_state:
    st.session_state.history = [] 

def main():
    # Setup styles and page structure
    setup_page()
    
    # Render Sidebar and get navigation choice
    page = render_sidebar()
    
    # Route to appropriate page
    if page == "✨ Code Studio":
        render_code_studio()
    elif page == "📊 Insights & Report":
        render_insights_report()
    elif page == "📜 History":
        render_history()

if __name__ == "__main__":
    main()
