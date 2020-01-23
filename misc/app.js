const express = require('express')
const app = express();
const fs = require('fs')

fs.readFile('json.json', 'utf8', function (err, data) {
    if (err){
     console.log(err)
    }
    payload = data;
   });


app.get('/json', (req, res) => {
    return res.status(200).send(payload)
});

app.listen(8080, function(err){
    if(err){
        console.log('error');
        return;
}
console.log('server listening on localhost:'+ 8080 )
})