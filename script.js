let pyodide;

async function loadPyodide() {
    pyodide = await loadPyodide();
    console.log("Pyodide loaded successfully!");
}

async function runPython() {
    let code = document.getElementById("python-code").value;
    let outputElement = document.getElementById("output");

    try {
        let result = await pyodide.runPythonAsync(code);
        outputElement.textContent = result;
    } catch (error) {
        outputElement.textContent = "Error: " + error;
    }
}

// Load Pyodide when the page loads
loadPyodide();
