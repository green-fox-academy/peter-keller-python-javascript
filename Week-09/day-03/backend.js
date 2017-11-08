var express = require('express');
var app = express();
var bodyParser = require('body-parser')
const jsonParser = bodyParser.json();

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

app.get('/appenda/:animal', function(request, response) {
    if (request.params.animal !== undefined) {
        response.json({"appended": request.params.animal + "a"});
    }
});

app.post('/dountil/:what', jsonParser, function(request, response) {
    let result;
    if (request.params.what ==="sum") {
        var sum = 0;
        for (var index = 0; index < request.body.until + 1; index++) {
            sum += index;
        }
        result = {"result": sum};
    } else if (request.params.what ==="factor") {
        var factorio = 1;
        for (var index = 1; index < request.body.until + 1; index++) {
            factorio *= index;
        }
        result = {"result": factorio};
    }
    response.json(result)
});

app.listen(8080);