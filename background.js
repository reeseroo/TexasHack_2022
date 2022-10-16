const api_url = "http://127.0.0.1:5000";



function getInput() {
  document.getElementById("userInput").innerHTML = 'data'
};

async function getPercentage(url) {

    const response = await fetch(url);

    var data = await response.json();
    console.log(data);
    if (response) {
        console.log(response);
    }
}

document.getElementById("myButton".addEventListener("click", getInput));
getPercentage(api_url);
