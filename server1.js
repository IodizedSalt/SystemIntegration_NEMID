const express = require('express')
var app = express();
var request = require('request')
var bodyParser = require('body-parser');
const fs = require('fs');
const $ = require('cheerio')
const jwt = require('jsonwebtoken')
const sqlite3 = require('sqlite3').verbose();


app.use(bodyParser.json());

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/css'));

PORT_NUM = 8080
var skatDatabase = new sqlite3.Database('./db/skat.db');


app.listen(PORT_NUM, function(err){
    if(err){
        console.log('error');
        return;
}
console.log('server listening on localhost:'+ PORT_NUM )



})
app.get('/', (req, res) => {
    res.sendFile(__dirname + "/index.html");
});

app.post('/token', function(req, res){
    let tokenData = jwt.decode(req.body.token)
    // console.log(tokenData)
    let tokenEmail = tokenData.email
    let sql = `SELECT balance Balance FROM users WHERE email = ?`

    skatDatabase.each(sql, [tokenEmail], (err, row) => {
        if (err) {
            throw err;
        }
        // this needs to respond with JSON??
        // res.send(`${tokenEmail}:\n\nYour bank account balance is ${row.Balance}kr.`)
        res.json({
            userEmail: tokenEmail,
            userSkatBalance: row.Balance
        });
    });

})

process.on('SIGINT', () => {
    skatDatabase.close();
});