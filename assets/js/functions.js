function renderSkat(userInformationJSON){
    document.getElementById("view-button-skat").hidden = false

    document.getElementById("view-button-skat").addEventListener("click", function() {
        document.getElementById("user-information-json").hidden = false;
        document.getElementById("user-name").hidden = false;
        displaySkat(userInformationJSON);
    }, false);

}

function displaySkat(userInformationJSON){

    let skatField = document.getElementById("user-skat-balance");
    let skatBalance = JSON.parse(userInformationJSON)['userSkatBalance']
    skatField.innerText = skatBalance;


}

function renderBank(userInformationXML){
    document.getElementById("view-button-bank").hidden = false

    document.getElementById("view-button-bank").addEventListener("click", function() {
        document.getElementById("user-information-xml").hidden = false;
        document.getElementById("user-name").hidden = false;

        var p = new DOMParser()
        xmldoc = p.parseFromString(userInformationXML, 'text/xml')
        var balance = xmldoc.getElementsByTagName("Balance")[0].innerHTML;
        displayBank(balance);
    }, false);

}

function displayBank(userInformationXML){
    let bankField = document.getElementById("user-bank-balance");    
    bankField.innerText = userInformationXML;

}

