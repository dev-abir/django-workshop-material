function calc(operation) {
    const a = parseInt(document.getElementById("inpA").value || 0);
    const b = parseInt(document.getElementById("inpB").value || 0);

    let c = 0;

    switch (operation) {
        case "+":
            c = a + b;
            console.log(c);
            break;
        case "-":
            c = a - b;
            break;
        case "/":
            c = a / b;
            break;
        case "*":
            c = a * b;
            break;
    }

    document.getElementById("taSol").value = c;
    // document.getElementById("taSol").innerText = c;
}

document.getElementById("btnAdd").addEventListener("click", () => calc("+"));
document.getElementById("btnSub").addEventListener("click", () => calc("-"));
document.getElementById("btnDiv").addEventListener("click", () => calc("/"));
document.getElementById("btnMul").addEventListener("click", () => calc("*"));
