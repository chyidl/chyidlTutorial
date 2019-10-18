var http = require('http');

// create an HTTP server object
http.createServer(function (req, res) {

    console.log(req.url);

    // status code, response headers
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('Hello World!');
    res.end();
}).listen(8080);

console.log('node running -> PORT 8080');
