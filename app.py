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

# Add a message to the app to indicate SQL, JSON, HTML, and JavaScript compatibility
st.write("SQL, JSON, HTML, and JavaScript compatible")

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
            script_tags = soup.find_all('script')
            if len(script_tags) == 1:
                script_code = script_tags[0].string.strip()
                if re.search(r'(\bconst\b|\blet\b|\bvar\b|\bfunction\b|\bif\b|\belse\b|\bfor\b|\bwhile\b|\bswitch\b)', script_code):
                    language = "JavaScript"
                    code_input = script_code
                else:
                    language = "HTML"
            else:
                try:
                    js_keywords_regex = r'(\bconst\b|\blet\b|\bvar\b|\bfunction\b|\bif\b|\belse\b|\bfor\b|\bwhile\b|\bswitch\b)'
                    match = re.search(js_keywords_regex, code_input.strip(), re.IGNORECASE)
                    if match:
                        language = "JavaScript"
                    else:
                        st.error("Unable to detect code language")
                        st.stop()
                except:
                    st.error("Unable to detect code language")
                    st.stop()
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
elif language == "HTML":
    soup = BeautifulSoup(code_input, 'html.parser')
    formatted_code = soup.prettify()
elif language == "JavaScript":
    try:
        formatted_code = autopep8.fix_code(code_input, options={'max_line_length': 120})
        formatted_code = formatted_code.strip()  # Remove any leading/trailing whitespaces
    except:
        st.error("Unable to format JavaScript code")
        st.stop()

# Display the formatted code and detected language
st.subheader(f"Formatted {language} code:")
st.code(formatted_code, language=language)