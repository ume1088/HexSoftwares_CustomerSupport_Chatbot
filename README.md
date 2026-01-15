# HexSoftwares_CustomerSupport_Chatbot
AI-Powered Customer Support Chatbot using Flask and Hugging Face Transformers. Provides FAQ-based instant answers with safe AI fallback and a clean web chat interface.
---
## 📌 Project Overview
This project demonstrates how AI can be safely integrated into a customer support system.  
Instead of relying fully on generative AI, the chatbot first checks a curated FAQ database and only uses AI when necessary.

This approach ensures:
- Accurate responses
- Reduced hallucinations
- Production-like safety design

---

## 🚀 Features
- FAQ-based instant responses
- AI fallback using DistilGPT-2
- Controlled prompt and output length
- Clean and simple chat UI
- Full-stack implementation
- Beginner-friendly and internship-ready project

---

## 🛠️ Tech Stack
    Backend:  Python, Flask  
    AI Model:  Hugging Face Transformers (DistilGPT-2)  
    Frontend:   HTML, CSS, JavaScript  

---

## ⚙️ Working Flow
1. User sends a message via the chat interface.
2. Backend checks for keyword matches in the FAQ database.
3. If found, a predefined response is returned.
4. If not found, a restricted AI-generated response is provided.
5. If AI output is unsafe or unclear, the user is redirected to support.

---

## 📂 Project Structure
HexSoftware_CustomerSupport_Chatbot/
│── app.py
│── requirements.txt
│
├── templates/
│ └── index.html
│
├── static/
│ ├── style.css
│ ├── script.js
│ └── bot.png



## 🧑‍💻 Installation & Usage

### 1️⃣ Clone the Repository

git clone https://github.com/ume1088/ HexSoftware_CustomerSupport_Chatbot.git
cd HexSoftware_CustomerSupport_Chatbot

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
python app.py

4️⃣ Open in Browser
http://127.0.0.1:5000/

🔒 AI Safety Measures
FAQ responses are prioritized over AI output

AI response length is restricted

Unsafe or unclear responses are blocked

Users are redirected to human support when required



👩‍💻 Author
Ume Habiba
BS IT Student
Aspiring AI & Machine Learning Engineer



