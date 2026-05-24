const button = document.getElementById("submitCode");


button.addEventListener("click", sendToBackend);

function sendToBackend() {
    let text = document.getElementById("textBox").value.trim();
    const language = document.getElementById("languageSelect").value;
    const passcode = document.getElementById("passcodeBox").value;

    // Basic input validation
    if (text.length === 0) {
        alert("Input cannot be empty");
        return;
    } 

    if (text.length > 5000) {
        alert("Input too long");
        return;
    } 
    // diable button and change text while waiting for response
    button.disabled = true;
    button.textContent = "Sending...";

    //for live website, replace other fetch
    //fetch("https://web.williamodavis.me/submit", {

    fetch("http://127.0.0.1:5000/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text, language: language, passcode: passcode })
    })
    .then(res => res.json())
    .then(data => {

    const output = document.getElementById("output");

    output.textContent = "";
     // Check for status in the response and display it if it's not "ok"
    if (data.status && data.status !== "ok") {
        output.textContent += `Status: ${data.status}\n\n`;
    }
    // divides up hjson string into individual vulnerabilities and formats them for display
    let vulnerabilities = data.message;
    if (typeof vulnerabilities === "string") {
    try {
        vulnerabilities = JSON.parse(vulnerabilities);
    } catch (e) {
        vulnerabilities = []; // If parsing fails, treat it as no vulnerabilities
    }
    }

    if (vulnerabilities.length === 0) {
    output.textContent = "No vulnerabilities found.";
    document.getElementById("resultsHeader").classList.remove("hidden");
    output.classList.remove("hidden");
    return; // Exit early if no vulnerabilities to display
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