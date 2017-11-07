'use strict';
var test = require('tape');
var apple = require('./apples');


test('return apple', function (t) {
  var actual = apple.getApple();
  var expected = "apple";

  t.equal(actual, expected);
  t.end();

});