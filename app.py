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
from bs4 import BeautifulSoup

st.title("🩺 Code Formatter")

# Add a message to the app to indicate SQL, JSON and HTML compatibility
st.write("SQL, JSON and HTML compatible")

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
        try:
            soup = BeautifulSoup(code_input, 'html.parser')
            language = "HTML"
        except:
            st.error("Unable to detect code language")
            st.stop()

# Format the code using the appropriate formatter
if language == "SQL":
    formatted_code = sqlparse.format(code_input, reindent=True)
    formatted_code = textwrap.indent(formatted_code, " " * 4)
elif language == "JSON":
    try:
        parsed_json = json.loads(code_input)
        formatted_code = json.dumps(parsed_json, indent=4, sort_keys=True)
    except ValueError:
        st.error("Invalid JSON syntax")
        st.stop()
else: # language == "HTML"
    soup = BeautifulSoup(code_input, 'html.parser')
    formatted_code = soup.prettify()

# Display the formatted code and detected language
st.subheader(f"Formatted {language} code:")
st.code(formatted_code, language=language)