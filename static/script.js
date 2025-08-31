async function safeFetch(url, payload) {
    try {
        const res = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        return await res.json();
    } catch {
        return { status: "warning", message: "Server error or offline." };
    }
}

function renderResult(box, { status, message }) {
    box.className = "result-" + status;
    box.innerText = message;
}

async function checkURL() {
    const url = document.getElementById("urlInput").value;
    const resultBox = document.getElementById("result");
    resultBox.innerText = "Checking...";
    const data = await safeFetch("/url-check", { url });
    renderResult(resultBox, data);
}

async function checkEmail() {
    const email = document.getElementById("emailInput").value;
    const resultBox = document.getElementById("result");
    resultBox.innerText = "Checking...";
    const data = await safeFetch("/email-check", { email });
    renderResult(resultBox, data);
}
