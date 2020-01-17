const express = require('express')
var app = express();
var bodyParser = require('body-parser');
const jwt = require('jsonwebtoken')
const sqlite3 = require('sqlite3').verbose();

app.use(bodyParser.json());

app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static(__dirname + '/assets'));
app.engine('html', require('ejs').renderFile);



PORT_NUM = 8080

app.listen(PORT_NUM, function(err){
    if(err){
        console.log('error');
        return;
}
console.log('server listening on localhost:'+ PORT_NUM )
})


app.get('/', (req, res) => {
    res.sendFile(__dirname + "/assets/views/index.html");
});

app.get('/account', (req, res) => {
    res.sendFile(__dirname + "/assets/views/account.html");
});

app.get('/logout', (req, res) => {
    res.redirect("/")
});

app.post('/login', (req, res) => {

        res.redirect("/account");
});

