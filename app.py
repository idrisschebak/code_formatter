import streamlit as st
import sqlparse
import textwrap
import pygments
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter
from yapf.yapflib import yapf_api
import autopep8

st.title("🩺 SQL Code Formatter")

code_input = st.text_area("Enter your code here", height=400)

language = "SQL"

if st.button("Format"):
    if language == "SQL":
        formatted_code = sqlparse.format(code_input, reindent=True)
        formatted_code = textwrap.indent(formatted_code, " " * 4)
    else:
        # Display an error message if the language is not compatible
        st.error("Sorry, this coding language is not (yet) compatible")
        pass

    # Display the formatted code and detected language
    st.subheader(f"Formatted {language} code:")
    st.code(formatted_code, language=language)