import streamlit as st
import sqlparse
import textwrap
import pygments
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter
import json
import yaml

st.title("🩺 Code Formatter")

code_input = st.text_area("Enter your .json, .py or .sql code here", height=400)

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
    elif language == "JSON":
        formatted_code = json.dumps(json.loads(code_input), indent=4)
    elif language == "YAML":
        formatted_code = yaml.dump(yaml.load(code_input), indent=4)
    else:
        # Use black to format non-SQL code
        formatted_code = black.format_str(code_input, mode=black.FileMode())

    # Display the formatted code and detected language
    st.subheader(f"Formatted {language} code:")
    st.code(formatted_code, language=language)
