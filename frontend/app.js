async function askBot() {
  const question = document.getElementById("question").value;
  const responseBox = document.getElementById("response");

  responseBox.textContent = "Thinking... 🤔";

  const res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: question })
  });

  const data = await res.json();
  responseBox.textContent = data.reply || "No reply from CryptoBuddy 😓";
}