const api_url = "http://127.0.0.1:5000";

async function getPercentage(url) {

    const response = await fetch(url);

    var data = await response.json();
    console.log(data);
    if (response) {
        getInput();
    }
    show(data);
}

getPercentage(api_url);

function getInput() {
    document.getElementById('userInput').innerHTML = data;
}
