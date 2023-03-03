import streamlit as st
import sqlparse
import textwrap
import pygments
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter

st.title("Code Formatter")

code_input = st.text_area("Enter code here", height=400)

try:
    # Try to detect the language of the input code
    lexer = get_lexer_by_name(pygments.lexers.guess_lexer(code_input).name)
    language = lexer.name
except pygments.util.ClassNotFound:
    # Default to SQL if language detection fails
    language = "SQL"

if st.button("Format"):
    if language == "SQL":
        formatted_code = sqlparse.format(code_input, reindent=True)
        formatted_code = textwrap.indent(formatted_code, " " * 4)
    else:
        # Use black to format non-SQL code
        formatted_code = black.format_str(code_input, mode=black.FileMode())

    st.text_area("Formatted code", value=formatted_code, height=400)