const sendBtn = document.getElementById("send-btn");
const input = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");

sendBtn.onclick = sendMessage;

input.addEventListener("keypress", function (e) {
    if (e.key === "Enter") sendMessage();
});

function sendMessage() {
    const msg = input.value.trim();
    if (!msg) return;

    chatBox.innerHTML += `
        <div class="user-msg">
            <span>${msg}</span>
        </div>
    `;
    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        chatBox.innerHTML += `
            <div class="bot-msg">
                <img src="/static/bot.png">
                <span>${data.reply}</span>
            </div>
        `;
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}