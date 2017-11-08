var express = require('express');
var app = express();

app.use('/assets', express.static('./assets'));

app.get('/', function(request, response) {
    response.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function(request, response) {
    let responseAnswer = {"error": "Gimme num"};
    if (request.query.input !== undefined) { 
        responseAnswer = {"received": request.query.input*1, "result": request.query.input*2};
    }
    response.json(responseAnswer);
});

app.listen(8080);