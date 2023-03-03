import sqlfluff
import streamlit as st
import black

def format_sql(sql_code):
    try:
        # Use sqlfluff to format the SQL code
        formatted_code = sqlfluff.format(sql_code, encoding='utf-8')
    except ImportError:
        # If sqlfluff is not available, use sqlparse as a fallback
        formatted_code = sqlparse.format(sql_code, reindent=True, keyword_case='upper')
    return formatted_code

def format_python(py_code):
    return black.format_str(py_code, mode=black.FileMode())

def main():
    st.title("Code Formatter")
    code_type = st.sidebar.radio("Select Code Type", ["SQL", "Python"])

    if code_type == "SQL":
        st.subheader("SQL Formatter")
        sql_code = st.text_area("Enter SQL Code Here", height=300)
        if st.button("Format SQL"):
            formatted_code = format_sql(sql_code)
            st.text_area("Formatted SQL Code", value=formatted_code, height=300)

    else:
        st.subheader("Python Formatter")
        py_code = st.text_area("Enter Python Code Here", height=300)
        if st.button("Format Python"):
            formatted_code = format_python(py_code)
            st.text_area("Formatted Python Code", value=formatted_code, height=300)

if __name__ == "__main__":
    main()