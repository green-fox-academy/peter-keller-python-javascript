'use strict';


const mysql = require('mysql');
const express = require('express');
const app = express();
var books = 'SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast JOIN author ON book_mast.aut_id = author.aut_id JOIN category ON book_mast.cate_id = category.cate_id JOIN publisher ON book_mast.pub_id = publisher.pub_id ';

express.json.type = 'application/json';

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
    return;
    }
    console.log("Connection estabilished");
});

app.get('/', function(request, response) {
    response.sendFile(__dirname + '/index.html');
});

app.get('/list', function(request, response) {
    connection.query('SELECT book_name FROM book_mast', function(err, rows) {
        //console.log(rows)
        if (err) {
            console.log(err.toString());
            return;
        };
        response.send(rows)
    });
    
    console.log("Data received from database");
    });



app.get('/booksdata', function(request, response) {
    connection.query(books, function(err, rows) {
        if (err) {
            console.log(err.toString());
            return;
    };
    console.log("Data received from database");
    let htmlString = '<table>';
    rows.forEach(function(row) {
        htmlString += '<tr><td>' + row.book_name + '</td><td>' + row.aut_name + '</td><td>' + row.cate_descrip + '</td><td>' + row.pub_name + '</td><td>' + row.book_price + '</td></tr>';
    });
    htmlString = htmlString + '</table>';
    response.send(htmlString)
    });
});


//app.get('/books', function(request, response) {
//    connection.query(place, function(err, rows) {
    //    if (err) {
  //          console.log(err.toString());
//            return;
 //       } else if (request.query.category) {
            
//        }
//        console.log(request.query.category)
       //console.log(rows)
//    let result = '<ul>'
//    rows.forEach(function(row) {
//        result = result += '<li>' + row.book_name + '</li>' ;
//    });
//    result = result + '</ul>';
//    console.log("Selected data received from database");

//    response.send(result);
//});
//});
app.listen(3000);