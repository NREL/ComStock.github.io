let pyodide;

async function loadPyodide() {
    pyodide = await loadPyodide();
    console.log("Pyodide loaded successfully!");
}

async function calculate() {
    let num1 = document.getElementById("num1").value;
    let num2 = document.getElementById("num2").value;
    
    let pythonCode = `
def add_numbers(a, b):
    return a + b

result = add_numbers(${num1}, ${num2})
`;

    try {
        await pyodide.runPythonAsync(pythonCode);
        let result = pyodide.globals.get("result");
        document.getElementById("output").textContent = result;
    } catch (error) {
        document.getElementById("output").textContent = "Error: " + error;
    }
}

// Load Pyodide on page load
loadPyodide();
