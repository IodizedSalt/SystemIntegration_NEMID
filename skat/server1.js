const express = require('express')
var app = express();
var bodyParser = require('body-parser');
const jwt = require('jsonwebtoken')
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors')

app.use(bodyParser.json());
app.use(cors())

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/assets'));
app.engine('html', require('ejs').renderFile);

// PORT_NUM = 8080
var skatDatabase = new sqlite3.Database('./skat.db');


PORT_NUM = 8079

app.listen(PORT_NUM, function(err){
    if(err){
        console.log('error');
        return;
}
console.log('server listening on localhost:'+ PORT_NUM )
})

app.post('/token', function(req, res){

    // let tokenData = jwt.decode(req.body.token, 'exampleKey')
    let tokenData = jwt.verify(req.body.token, "example_key")

    let tokenEmail = tokenData.email
    let tokenName = tokenData.name

    let sql = `SELECT balance Balance FROM users WHERE email = ?`

    skatDatabase.each(sql, [tokenEmail], (err, row) => {
        if (err) {
            throw err;
        }
        res.json({
            userEmail: tokenEmail,
            userSkatBalance: row.Balance,
            userName: tokenName
        });
    });

})


// app.listen(PORT_NUM, function(err){
//     if(err){
//         console.log('error');
//         return;
// }
// console.log('server listening on localhost:'+ PORT_NUM )

// })
// app.get('/', (req, res) => {
//     res.sendFile(__dirname + "/assets/views/index.html");
// });

// app.get('/account', (req, res) => {
//     //figure out how to send this file, doesnt update
//     res.sendFile(__dirname + "/assets/views/account.html");
// });

// app.post('/login', (req, res) => {

//     console.log(req.body.item)
//     if(req.body.item){
//         res.redirect("/account");
//     }

// });


process.on('SIGINT', () => {
    skatDatabase.close();
});