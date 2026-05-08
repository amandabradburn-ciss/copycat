from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import tempfile
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "CopyCat backend is running."

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    code = data.get("text", "")

    if not code.strip():
        return jsonify({"message": "No code submitted."}), 400

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as temp_file:
            temp_file.write(code)
            temp_file_path = temp_file.name

        result = subprocess.run(
            ["bandit", temp_file_path],
            capture_output=True,
            text=True
        )

        os.remove(temp_file_path)

        output = result.stdout

        if not output.strip():
            output = "No security issues found."

        return jsonify({"message": output})

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)