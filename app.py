from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# -----------------------------
# AI MODEL (safe fallback only)
# -----------------------------
generator = pipeline(
    "text-generation",
    model="distilgpt2",
    max_new_tokens=40,
    do_sample=True,
    temperature=1
)

# -----------------------------
# FAQ DATABASE (main answers)
# -----------------------------
FAQS = {
    "hello":"Hyy, ask me anything about us",
    "return": "Our return policy lasts 30 days from the date of purchase 😊.",
    "refund": "Refunds are processed within 5–7 business days after approval.",
    "track": "You can track your order using the tracking link sent to your email.",
    "order": "Order details and tracking information are sent to your email.",
    "contact": "You can contact our support team at support@example.com.",
    "hours": "Our support hours are Monday to Friday, 9 AM to 6 PM ⏰.",
    "location": "We operate online and serve customers worldwide.",
    "services": "We provide customer support and AI-powered solutions.",
    "payment": "We accept all major credit cards, PayPal, and other online payment methods.",
    "shipping": "Standard shipping takes 5–10 business days. Expedited shipping is available.",
    "cancellation": "You can cancel your order within 24 hours of placing it.",
    "account": "You can manage your account settings from the profile section.",
    "pricing": "All product prices are listed on the website and include taxes.",
    "warranty": "Products come with a 1-year warranty for manufacturing defects.",
    "support": "For technical issues, please reach out to our support team at support@example.com.",
    "subscription": "You can manage or cancel your subscription anytime from your account.",
    "feedback": "We value your feedback! You can submit it through the contact form on our website."

}

def get_faq_reply(message: str):
    msg = message.lower()
    for keyword, answer in FAQS.items():
        if keyword in msg:
            return answer
    return None

# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    # 1️⃣ FAQ FIRST (accurate)
    faq_reply = get_faq_reply(user_message)
    if faq_reply:
        return jsonify({"reply": faq_reply})

    # 2️⃣ AI FALLBACK (restricted)
    prompt = (
        "You are a professional customer support agent.\n"
        "Answer clearly in 1 short sentence.\n"
        "If unsure, say: 'Please just ask customer support related questions'.\n\n"
        f"Customer question: {user_message}\n"
        "Answer:"
    )

    try:
        result = generator(prompt)[0]["generated_text"]
        reply = result.split("Answer:")[-1].strip()

        # Safety cleanup
        if len(reply) > 200 or "Custom Code" in reply:
            reply = "Please contact support@example.com for further assistance."

    except Exception:
        reply = "Sorry, I'm having trouble answering that right now."

    return jsonify({"reply": reply})

# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)