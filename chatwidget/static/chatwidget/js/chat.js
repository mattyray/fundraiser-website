document.addEventListener("DOMContentLoaded", () => {
  const $chatToggle = document.getElementById("ai-chatbot-toggle");
  const $chatWidget = document.getElementById("ai-chatbot");
  const $chatInput = document.getElementById("ai-chatbot-input-field");
  const $chatBody = document.getElementById("ai-chatbot-body");
  const $chatClose = document.getElementById("ai-chatbot-close");

  // Open chat
  $chatToggle.addEventListener("click", () => {
    $chatWidget.classList.add("show");
    $chatWidget.style.display = "flex";
    $chatInput.focus();
  });

  // Close chat
  $chatClose.addEventListener("click", () => {
    $chatWidget.classList.remove("show");
    setTimeout(() => {
      $chatWidget.style.display = "none";
    }, 300);
  });

  // Handle message send
  $chatInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && $chatInput.value.trim() !== "") {
      e.preventDefault();
      const userMessage = $chatInput.value.trim();
      $chatInput.value = "";
      appendMessage("user", userMessage);
      showTyping();

      fetch("/chatwidget/api/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
      })
        .then(res => res.json())
        .then(data => {
          removeTyping();
          appendMessage("ai", data.reply || data.error || "*⚠️ No reply*");
        })
        .catch(() => {
          removeTyping();
          appendMessage("ai", "*⚠️ An error occurred. Please try again.*");
        });
    }
  });

  // Add chat message
  function appendMessage(sender, text) {
    const msg = document.createElement("div");
    msg.className = `chat-message ${sender} fade-in`;
    msg.innerHTML = window.marked ? marked.parse(text) : text;
    $chatBody.appendChild(msg);
    $chatBody.scrollTop = $chatBody.scrollHeight;
  }

  // Typing placeholder
  let typingEl = null;
  function showTyping() {
    typingEl = document.createElement("div");
    typingEl.className = "chat-message ai fade-in";
    typingEl.innerHTML = "<em>Typing...</em>";
    $chatBody.appendChild(typingEl);
    $chatBody.scrollTop = $chatBody.scrollHeight;
  }

  function removeTyping() {
    if (typingEl && typingEl.parentNode) {
      typingEl.parentNode.removeChild(typingEl);
      typingEl = null;
    }
  }
});
