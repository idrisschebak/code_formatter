# Snake Game
This is a Streamlit app that can format SQL, JSON, and YAML code. The app uses sqlparse to format SQL code, json library to format JSON code, and yaml library to format YAML code. For non-SQL code, it uses the black library.


### 📦 Installation

Clone the repository:

```git clone https://github.com/yourusername/code-formatter.git ```

Install the dependencies:

```pip install -r requirements.txt```

### 🚀 Usage

Run the app:

```streamlit run app.py```

- Enter the code you want to format in the text area.

- Click the "Format" button.

- The app will format the code and display it below the text area.

- If the code is SQL, it will be formatted using sqlparse.
- If the code is JSON, it will be formatted using the json library.
- If the code is YAML, it will be formatted using the yaml library.
- For any other code, it will be formatted using black.

### 💡 Reporting Bugs and Contributing
If you encounter any bugs or would like to suggest new features, please create an issue on the GitHub repository. Contributions are also welcome! If you would like to contribute to Kitsec, please create a pull request on the GitHub repository.

### 🔖 License
Kitsec is licensed under the MIT License.