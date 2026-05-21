from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv
import sys
import subprocess
import tempfile
import os
import json

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No API key found.")

app = Flask(__name__)
CORS(app)
client = genai.Client(api_key=api_key)

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
            [sys.executable, "-m", "bandit", "-f", "json", temp_file_path],
            capture_output=True,
            text=True
        )

        os.remove(temp_file_path)

        bandit_output = result.stdout

        if not bandit_output.strip():
            bandit_output = "No security issues found."

        prompt = f"""
        You are a programmer evaluating the security of a section of Python code that someone else wrote. You ran the code through Bandit and got the below output.
        For each vulnerability or issue found by Bandit, give a short 1 sentence explanation of what the issue is, and a short 1 sentence explanation of how to fix it.
         - If the fix explanation requires more text, you may go up to 2 or 3 sentences in length, but try to avoid that when possible.
         - Choose your words as if you were talking to a novice/intermediate programmer.
         - IMPORTANT: Do NOT analyze the code for any vulnerabilities yourself, go off what Bandit reports.

        Input Code
        <input_code>
        {code}
        </input_code>

        Bandit Output
        <bandit_output>
        {bandit_output}
        </bandit_output>
    
        ONLY RESPOND WITH THE FOLLOWING FORMAT - DO NOT RESPOND IN ANY OTHER WAY!!!!!!
        For each vulnerability, return a block in the example format below with each block separated by a single line. Include an opening and closing [] at the beginning and end.
        {{
            "Vulnerability": "1 sentence explanation of vulnerability",
            "Severity": "Severity of vulnerability - Use Bandit's scale. (i.e. "HIGH", "MEDIUM", "LOW")",
            "CWE": "Return CWE info passed from Bandit. Response should be just the number - i.e. "89" instead of "CWE-89", "CWE 89" or other variations.",
            "Suggested Fix": "Short explanation of how to fix issue. Do not go over 1 to 2 sentences unless absolutely necessary. Do not include line numbers telling where error is.",
            "Line #": "Line number(s) where vulnerability is. Either format like "156", "156-160", or "156,160,""
        }}
        

        """

        prompt = prompt.replace("\r\n", "\n").replace("\r", "")
        response = client.models.generate_content(
            # local testing
             model = "gemini-2.5-flash",

            # live website
            #model = "gemini-3.1-flash-lite",
            contents = prompt,
            config = genai.types.GenerateContentConfig(response_mime_type="application/json",)
        )

        raw_text = response.text.strip()
        if raw_text.startswith("```"):
            raw_text = raw_text.strip("`").strip()
            if raw_text.lower().startswith("json"):
                raw_text = raw_text[4:].strip()
        llm_response = json.loads(raw_text)
        #commented out for now, uncomment later for actually parsing info
        #return jsonify({"message": llm_response})

        #temp output display
        basic_text = json.dumps(llm_response, indent=4)
        return jsonify({"message": basic_text})

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
    #for live website
    #app.run(host="127.0.0.1", port="5000")