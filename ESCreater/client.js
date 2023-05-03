const API_URL = "https://guarded-beyond-83547.herokuapp.com/api/translate";

const promptInput = document.getElementById("prompt");
const companyPhilosophyInput = document.getElementById("company-philosophy");
const selfPrInput = document.getElementById("self-pr");
const wordCountInput = document.getElementById("word-count");
const generateButton = document.getElementById("generateButton");
const generatedEs = document.getElementById("generated-es");
const loading = document.getElementById("loading");

generateButton.addEventListener("click", async () => {
    loading.style.display = "block";
    const content = `私の自己PR：${selfPrInput.value}\nお題：${promptInput.value}\n企業理念：${companyPhilosophyInput.value}\n企業理念に対し再現性を意識して自己PRを結びつけ、お題に文字数${wordCountInput.value}以内で回答してください。`;
    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "content": content,
        }),
    });
    const data = await response.json();
    loading.style.display = "none";
    generatedEs.innerHTML = data.message.trim();
});
