import re
import streamlit as st
import sqlparse
import json
import textwrap
import pygments
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter
from yapf.yapflib import yapf_api
import autopep8

st.title("🩺 Code Formatter")

# Add a message to the app to indicate SQL and JSON compatibility
st.write("SQL and JSON compatible")

code_input = st.text_area("Enter your code here", height=400)

# Check if code is entered
if not code_input:
    st.stop()

# Detect the language of the code
sql_keywords_regex = r'^(SELECT|WITH|INSERT|UPDATE|DELETE|CREATE|DROP|ALTER)'
match = re.search(sql_keywords_regex, code_input.strip(), re.IGNORECASE)
if match:
    language = "SQL"
else:
    try:
        json.loads(code_input)
        language = "JSON"
    except ValueError:
        st.error("Unable to detect code language")
        st.stop()

# Format the code using the appropriate formatter
if language == "SQL":
    formatted_code = sqlparse.format(code_input, reindent=True)
    formatted_code = textwrap.indent(formatted_code, " " * 4)
else:
    try:
        parsed_json = json.loads(code_input)
    except ValueError:
        st.error("Invalid JSON syntax")
        st.stop()

    formatted_code = json.dumps(parsed_json, indent=4, sort_keys=True)

# Display the formatted code and detected language
st.subheader(f"Formatted {language} code:")
st.code(formatted_code, language=language)