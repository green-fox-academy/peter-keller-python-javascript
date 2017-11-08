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

app.get('/greeter', function(request, response) {
    if (request.query.name === undefined) {
        response.json({"error": "Please provide name"});
    } else if (request.query.title === undefined) {
        response.json({"error": "Please provide title"});
    } else {
        response.json({"Welcome message": "Oh hi there " + request.query.name + " my dear " + request.query.title})
    }
});

app.listen(8080);