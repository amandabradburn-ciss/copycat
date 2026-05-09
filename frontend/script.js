const button = document.getElementById("submitCode");

button.addEventListener("click", sendToBackend);

function sendToBackend() {
    let text = document.getElementById("textBox").value;

    //for live website, replace other fetch
    //fetch("https://web.williamodavis.me/submit", {
    fetch("http://127.0.0.1:5000/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        const output = document.getElementById("output"); 
        output.classList.remove("hidden");
        output.innerText = data.message;
    });
}
