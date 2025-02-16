import streamlit as st
import google.generativeai as genai
import os

# Set up the API key
API_KEY = "AIzaSyDejubChBeArtssNcboIgj0-kFW38AYS2Q"  # Replace with your actual Google AI Key
genai.configure(api_key=API_KEY)

# Function to get AI feedback on the code
def review_code(code):
    prompt = f"""
    You are an expert Python code reviewer. Review the following Python code, identify any potential bugs or improvements, 
    and provide a corrected version of the code. If the code is perfect, just confirm it.

    Code:
    ```python
    {code}
    ```

    Response format:
    - **Issues Found:** List potential issues and their explanations.
    - **Fixed Code:** Provide a corrected version of the code.
    """

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="GenAI Code Reviewer", layout="wide")
st.title("GenAI App - AI Code Reviewer")

st.write("Submit your Python code below for an AI-powered review. The AI will detect bugs and suggest improvements.")

# Text area for user input
code_input = st.text_area("Enter your Python code:", height=250)

if st.button("Review Code"):
    if code_input.strip():
        with st.spinner("Analyzing your code..."):
            feedback = review_code(code_input)
        st.subheader("Review Feedback:")
        st.markdown(feedback)
    else:
        st.warning("Please enter Python code before submitting.")

st.markdown("---")
st.markdown("🚀 Built using **Streamlit** and **Google Gemini AI**")
