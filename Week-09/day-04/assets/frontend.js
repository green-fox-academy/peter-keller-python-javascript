'use strict';

let url = "http://localhost:3000";
let xhr = new XMLHttpRequest();
let ulElement = document.querySelector('ul');
let tableElement = document.querySelector('table');

function talkToApi(method, resource, callback){
    xhr.open(method, url + resource, true);
    xhr.onload = function(){
        callback(xhr.response);
    };
    xhr.send();
};

talkToApi('GET', '/booksdata', listDetails);

// more difficult solution:

/*
function createList(response) {
    let newList = JSON.parse(response);
    newList.books.forEach(function(element) {
        const template = `
        <li>${element.book_name}</li>
        `
        ulElement.innerHTML += template;
    });
}; */

// easier solution:

function createList(response) {
    let items = JSON.parse(response);
    items.books.forEach(function(element) {
        const listItems = '<li>' + element.book_name + '</li>';
        ulElement.innerHTML += listItems;
    });
};


