
'use strict';



var currentHours = 14;

var currentMinutes = 34;

var currentSeconds = 42;


console.log("Time remaining is: " + ((24 - currentHours - 1) * 3600 + (60 - currentMinutes - 1) * 60 + (60 - currentSeconds))); 
// Write a program that prints the remaining seconds (as an integer) from a

// day if the current time is represented by these variables