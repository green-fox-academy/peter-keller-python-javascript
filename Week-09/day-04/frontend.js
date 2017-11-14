'use strict'

let url = "http://localhost:3000";
let xhr = new XMLHttpRequest();

function talkToApi(method, resource, callback){
    xhr.open(method, url + resource, true);
    xhr.onload = function(){
        callback(xhr.response);
    };
    xhr.send();
};

talkToApi('GET', '/list', createList);

function createList(response) {
    console.log(response)
    let newList = JSON.parse(response);
    console.log(newList)
    let unorderedList = "<ul>";
    newList.forEach(function(element) {
        unorderedList = unorderedList + "<li>" + element.book_name + "</li>";
    });
    unorderedList = unorderedList + "</ul>";
};



//function createElement () {
//    let div = document.createElement('div');
//    div.innerHTML = connectionObject.response;
//    bodyElement.appendChild(div);
//}



