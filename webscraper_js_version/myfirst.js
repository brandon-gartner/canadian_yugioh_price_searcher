//basic http 
var http = require('http');

//file manipulation
var fs = require('fs');

//request promise
var rp = require('request-promise');

var url = 'https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States';

http.createServer(function (req, res) {
    fs.readFile('demofile1.html', function(err, data){
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        res.end();    
    });
}).listen(8080);