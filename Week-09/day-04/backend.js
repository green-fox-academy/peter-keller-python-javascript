'use strict';

const mysql = require('mysql');
const express = require('express');
const app = express();
express.json.type = 'application/json';

app.use(express.json());


var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'ridata94',
    database: 'bookstore'
});

connection.connect(function(err) {
    if (err) {
      console.log(err, "error");
    return
    }
    console.log('mysql server connected');
});

app.get('/', function(request, response) {
    response.sendFile(__dirname + '/index.html');
});

app.get('/list', function(request, response) {
    connection.query('SELECT book_name FROM book_mast;', function(err, rows){
        if(err){
            console.log(err.toString());
    };
    console.log("Data received from Db:\n");
    let htmlString = '<ul>';
    rows.forEach(function(row) {
        htmlString = htmlString + '<li>' + row.book_name + '</li>';
    });
    htmlString = htmlString + '</ul>';
    response.send(htmlString);
    });
});


app.listen(3000);