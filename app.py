from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient("mongodb+srv://testuser:test123@cluster0.ndnnwdz.mongodb.net/?appName=Cluster0")
db = client["intucate_db"]

@app.route('/')
def home():
    return "API is running"

@app.route('/ask', methods=['POST'])
def handle_question():
    try:
        data = request.get_json()

        if not data or "userInput" not in data:
            return jsonify({"error": "userInput is required"}), 400

        user_input = data["userInput"]

        prompt_data = db.prompts.find_one({"_id": "Education_Prompt"})

        if prompt_data is None:
            return jsonify({"error": "Prompt not found"}), 404

        template = prompt_data.get("template", "")

        final_text = template.replace("{{userInput}}", user_input)
        response_text = "Answer: " + user_input

        db.history.insert_one({
            "input": user_input,
            "response": response_text,
            "created_at": datetime.utcnow()
        })

        return jsonify({
            "response": response_text
        })

    except Exception as e:
        print("Error:", e)  # helpful for debugging
        return jsonify({"error": "Something went wrong"}), 500


if __name__ == "__main__":
    app.run(debug=True)