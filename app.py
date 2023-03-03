import streamlit as st
import sqlfluff
import black

st.title("Code Formatter")

language = st.selectbox("Select a language", ("SQL", "Python"))

code_input = st.text_area("Enter code here", height=400)

if st.button("Format"):
    if language == "SQL":
        formatted_code = sqlfluff.linter.lint_string(code_input)[0].as_string()
    elif language == "Python":
        formatted_code = black.format_str(code_input, mode=black.FileMode())
    else:
        formatted_code = ""

    st.text_area("Formatted code", value=formatted_code, height=400)