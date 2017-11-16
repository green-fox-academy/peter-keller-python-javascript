'use strict';

let url = "http://localhost:3000";
let xhr = new XMLHttpRequest();
let ulElement = document.querySelector('ul');
let tableElement = document.querySelector('tbody');

function talkToApi(method, resource, callback){
    xhr.open(method, url + resource, true);
    xhr.onload = function(){
        callback(JSON.parse(xhr.response));
    };
    xhr.send();
};

talkToApi('GET', '/books?category=Science', listByFilter);    

/*
if (document.location.href.indexOf("list") == -1) {
    talkToApi('GET', '/booksdata', listDetails);
} else { 
    talkToApi('GET', '/list', createList);    
};
*/

/*
 correct solution:

function createList(response) {
    let newList = JSON.parse(response);
    newList.books.forEach(function(element) {
        const template = `
        <li>${element.book_name}</li>
        `
        ulElement.innerHTML += template;
    });
};
easier solution: 
*/


function createList(response) {
    response.books.forEach(function(element) {
        const listItems = '<li>' + element.book_name + '</li>';
        ulElement.innerHTML += listItems;
    });
};


function listDetails(response) {
    response.books.forEach(function(element) {
        const listData = '<tr><td>' + element.book_name +
                         '</td><td>' + element.aut_name +
                         '</td><td>' + element.cate_descrip +
                         '</td><td>' + element.pub_name +
                         '</td><td>' + element.book_price +
                         '</td></tr>';
        tableElement.innerHTML += listData;
    });
};


function listByFilter(response) {
    response.forEach(function(elements) {
        const listedData = '<li>' + elements.book_name + '</li>';
        ulElement.innerHTML += listedData;
    });
};