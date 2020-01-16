function renderSkat(userInformationJSON){
    document.getElementById("view-button-skat").hidden = false

    document.getElementById("view-button-skat").addEventListener("click", function() {
        document.getElementById("user-information-json").hidden = false;
        document.getElementById("user-name").hidden = false;
        displaySkat(userInformationJSON);
    }, false);

}

function renderBank(userInformationXML){
    document.getElementById("view-button-bank").hidden = false
    //extract data from xml and pass to function
    document.getElementById("view-button-bank").addEventListener("click", function() {
        document.getElementById("user-information-xml").hidden = false;
        document.getElementById("user-name").hidden = false;
        displayBank(userInformationXML);
    }, false);

}

function displayBank(userInformationXML){

    let bankField = document.getElementById("user-bank-balance");
    // let xmlDiv = document.getElementById("user-information-xml")

    bankField.innerText = userInformationXML;

}

function displaySkat(userInformationJSON){
    console.log(userInformationJSON)


    let skatField = document.getElementById("user-skat-balance");
    // let jsonDiv = document.getElementById("user-information-json");

    skatField.innerText = userInformationJSON;  //Why does this not work
    // skatField.innerHTML = userInformationJSON;


}