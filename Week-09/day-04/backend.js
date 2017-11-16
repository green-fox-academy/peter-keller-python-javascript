'use strict';


const mysql = require('mysql');
const express = require('express');
const app = express();
var books = 'SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast JOIN author ON book_mast.aut_id = author.aut_id JOIN category ON book_mast.cate_id = category.cate_id JOIN publisher ON book_mast.pub_id = publisher.pub_id ';

express.json.type = 'application/json';

app.use("/assets", express.static("assets"));
app.use(express.json());



const connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "ridata94",
    database: 'bookstore'
});


connection.connect(function(err){
    if (err) {
        console.log("Cannot connect to database");
    } else { 
        console.log("Connection estabilished");
}});


app.get('/', function(request, response) {
    response.sendFile(__dirname + '/index.html');
});


app.get('/list', function(request, response) {
    connection.query(books, function(err, rows) {
        if (err) {
            console.log(err.toString());
        };
        response.send({'books': rows});
    });
    console.log("Data received from database");
});


app.get('/booksdata', function(request, response) {
    connection.query(books, function(err, rows) {
        if (err) {
            console.log(err.toString());
        };
        response.send({'books': rows});
    });
    console.log("Data received from database");
});


app.get('/books', function(request, response) {
    let dataLocation = 'SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast JOIN author ON book_mast.aut_id = author.aut_id JOIN category ON book_mast.cate_id = category.cate_id JOIN publisher ON book_mast.pub_id = publisher.pub_id ';    
    if (request.query.category) {
        dataLocation = dataLocation + ' WHERE cate_descrip = "' + request.query.category + '";';
    } else if (request.query.publisher) {
        console.log(request.query.publisher)
        dataLocation = dataLocation + ' WHERE pub_id = ' + request.query.publisher + ';';
    }
    connection.query(dataLocation, function(err, rows) {
        if (err) {
            console.log(err.toString());
        }
        response.send(rows);
        console.log("Selected data received from database");
        console.log(rows)
    });
});
/*
function getQueryVariable(anythin) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        if (decodeURIComponent(pair[0]) == variable) {
            return decodeURIComponent(pair[1]);
        }
    }
    console.log('Query variable %s not found', request.query);
}
*/
app.listen(3000);