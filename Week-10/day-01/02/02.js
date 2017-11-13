'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference


function rectangle(width, height) {
    this.width = width;
    this.height = height;
};

rectangle.prototype.getArea = function(width, height) {
    console.log(this.width * this.height);
};

rectangle.prototype.getCircumference = function(width, height) {
    console.log((this.width + this.height) * 2);
};

var something = new rectangle(2, 2);
something.getArea();
something.getCircumference();