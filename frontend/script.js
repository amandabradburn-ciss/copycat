const button = document.getElementById("submitCode");

button.addEventListener("click", sendToBackend);

function sendToBackend() {
    let text = document.getElementById("textBox").value.trim();

    if (text.length === 0) {
        alert("Input cannot be empty");
        return;
    }

    if (text.length > 5000) {
        alert("Input too long");
        return;
    }

    button.disabled = true;
    button.textContent = "Sending...";

    //for live website, replace other fetch
    //fetch("https://web.williamodavis.me/submit", {

    fetch("http://127.0.0.1:5000/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(res => res.json())
    .then(data => {

    const output = document.getElementById("output");

    output.textContent = `Status: ${data.status || "ok"}\n\n`;

    let vulnerabilities = data.message;

    if (typeof vulnerabilities === "string") {
        vulnerabilities = JSON.parse(vulnerabilities);
    }

    vulnerabilities.forEach((item, index) => {
        output.textContent +=
`[${index + 1}] ${item.Vulnerability}

Severity: ${item.Severity}
CWE: ${item.CWE}
Line: ${item["Line #"]}

Suggested Fix:
${item["Suggested Fix"]}

-----------------------------------

`;
    });

    document.getElementById("resultsHeader").classList.remove("hidden");
    output.classList.remove("hidden");
})

    .catch(err => {
        document.getElementById("output").textContent =
            "Error: unable to reach backend";
    })

    .finally(() => {
        button.disabled = false;
        button.textContent = "Submit";
    });
}