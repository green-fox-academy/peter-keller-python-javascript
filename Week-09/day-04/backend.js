'use strict';


const mysql = require('mysql');
const express = require('express');
const app = express();
var books = 'SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast JOIN author ON book_mast.aut_id = author.aut_id JOIN category ON book_mast.cate_id = category.cate_id JOIN publisher ON book_mast.pub_id = publisher.pub_id ';

express.json.type = 'application/json';
app.use("/assets", express.static("assets"));
app.use(express.json());



var connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "ridata94",
    database: 'bookstore'
});


connection.connect(function(err){
    if (err) {
        console.log("Error connection to database");
    };
    console.log("Connection estabilished");
});


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
    connection.query(books, function(err, rows) {
        books = 'SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast JOIN author ON book_mast.aut_id = author.aut_id JOIN category ON book_mast.cate_id = category.cate_id JOIN publisher ON book_mast.pub_id = publisher.pub_id ';
        
        if (err) {
            console.log(err.toString());
        } else if (request.query.category) {
            books = books + 'WHERE cate_descrip = "' + request.query.category + '";';
        }
        let result = '<ul>'
        rows.forEach(function(element) {
            result = result += '<li>' + element.book_name + '</li>' ;
        });
        result = result + '</ul>';
        console.log("Selected data received from database");

        response.send(result);
    });
});

app.listen(3000);