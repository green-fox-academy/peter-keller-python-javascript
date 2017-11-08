var express = require('express');
var app = express();

app.use('/assets', express.static('./assets'));

app.get('/', function(request, response) {
    response.sendFile(__dirname + '/index.html');
});

app.get("/doubling", function(request, response) {
    let responseNumber = {"received": request.query.input, "result": request.query.input*2};
    response.send(JSON.stringify(responseNumber));
});

app.listen(8080);