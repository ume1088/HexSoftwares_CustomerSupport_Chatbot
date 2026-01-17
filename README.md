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
✅ Accurate answers for Frequently Asked Questions (FAQs)
🤖 AI-based response generation using Hugging Face (distilgpt2) when no FAQ matches
🌐 Web-based chat interface
⚡ Fast and lightweight Flask backend
📁 Clean project structure with templates and static files

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

##💬 Example Questions (Recommended)
To get accurate responses, ask questions related to the FAQs, such as:
“What are your support hours?”
“How can I contact customer support?”
“What is your refund policy?”
“What services do you provide?”
“Where is your company located?”
For other questions, the chatbot will attempt an AI-generated response, which may be general in nature.
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

⚠️ Important Note
The AI model (distilgpt2) is not trained on company data
Best performance is achieved when asking FAQ-related questions
This project focuses on logic, structure, and learning, not enterprise-level AI



👩‍💻 Author
Ume Habiba
BS IT Student
Aspiring AI & Machine Learning Engineer
GitHub: https://github.com/ume1088


