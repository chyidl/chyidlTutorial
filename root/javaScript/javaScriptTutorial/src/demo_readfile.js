// reads the HTML file, and return the content
var http = require('http');
var fs = require('fs');

http.createServer(function (req, res) {
    // Read Files: used to read files on your computer.
    fs.readFile('demofile1.html', function(err, data) {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        res.end();
    });
}).listen(8080);

console.log('node server -> PORT 8080');
