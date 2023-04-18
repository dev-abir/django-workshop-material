const inpN = document.getElementById("inpN");

function inputChanged() {
    const n = parseInt(inpN.value || 0);

    let pattern = "";
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= i; j++) {
            pattern += j;
        }
        pattern += "\n";
    }
    document.getElementById("taPat").value = pattern;
}

inputChanged();
inpN.addEventListener("input", inputChanged);
