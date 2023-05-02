const API_URL = "https://guarded-beyond-83547.herokuapp.com/api/translate";

const inputText = document.getElementById("inputText");
const convertButton = document.getElementById("convertButton");
const outputText = document.getElementById("outputText");
const loading = document.getElementById("loading");

convertButton.addEventListener("click", async () => {
    loading.style.display = "block";
    const content = `文章を端的にビジネスメール風の丁寧な表現に変えてください：${inputText.value}`;
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
    outputText.innerHTML = data.message.trim();
});
