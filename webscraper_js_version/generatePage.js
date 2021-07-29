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
        // res.write(data);

        htmlText = scrapePres(url);
        res.write(htmlText);
        // console.log(htmlText + 'afdasdadfsfdafdas');
        res.end();    
    });
}).listen(8080);

function scrapePres(url){
    //request promise
    var rp = require('request-promise');
    var htmlText = "cccccccc";
    console.log('about to request')
    var response = rp(url)
        .then(function(html){
            console.log('found the html');
            //it succeeds
            
            //console.log(html);
            htmlText = 'aaaaaaaa';
            // return htmlText;
        }).catch(function(err){
            //handle error
            console.log('didnt find the html')
            htmlText = 'bbbbbbb';
            // return htmlText;
        });
        console.log('about to see response')
        console.log(response);
        // console.log('finished requesting')
        console.log()
        // return "Failed to find, ";
        return htmlText;
}