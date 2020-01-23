const http = require('http');

const options = {
    hostname: 'localhost',
    port: 8080,
    path: '/json',
    method: 'GET'
}

const req = http.request(options, res =>{
    res.on('data', d =>{
        process.stdout.write(d)
    })
})
req.end()

