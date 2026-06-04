AI Prompt-Based Response System

Overview

This project is a backend application built using Flask and MongoDB that processes user input and generates responses based on predefined prompt templates. It also stores all user interactions in a database for tracking and analysis.

The system is designed to simulate how prompt-based AI systems handle user queries in a structured way.

Features

* Accepts user input via REST API
* Retrieves prompt templates from MongoDB
* Generates responses based on input
* Stores user input, response, and timestamp
* Basic error handling and validation

Tech Stack

* **Backend:** Python (Flask)
* **Database:** MongoDB Atlas
* **Testing Tool:** Postman

Project Structure

```
app.py
requirements.txt
README.md
```

---

Installation & Setup

### 1. Clone the Repository

```
git clone <your-repo-link>
cd <your-project-folder>
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run the Application

```
python app.py
```

### 4. Server Runs On

```
http://127.0.0.1:5000
```

---

API Endpoint

### POST /ask

#### Request Body:

```
{
  "userInput": "Your question here"
}
```

#### Response:

```
{
  "response": "Answer: Your question here"
}
```

---

Database Structure

### 1. prompts collection

Stores prompt templates:

```
{
  "_id": "Education_Prompt",
  "template": "You are an expert. Answer this: {{userInput}}"
}
```

### 2. history collection

Stores:

* user input
* generated response
* timestamp

---

Testing

The API was tested using Postman by sending POST requests and verifying both the response and database storage.

---

Future Improvements

* Integrate AI models for dynamic responses
* Add user authentication
* Build a frontend interface
* Improve error handling and validation

---

Conclusion

This project demonstrates backend API development, database integration, and handling real-time user requests using Flask and MongoDB.

---
