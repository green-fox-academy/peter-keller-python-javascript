

'use strict';
var test = require('tape');
var sumNum = require('./sum');


test('sum numbers', function (t) {
  var actual = sumNum.sumElements([1, 2, 3]);
  var expected = 6

  t.equal(actual, expected);
  t.end();

});

test('one element', function (t) {
    var actual = sumNum.sumElements([2]);
    var expected = 2;

    t.equal(actual, expected);
    t.end();
});

test('empty list', function (t) {
    var actual = typeof sumNum.sumElements([]);
    var expected = typeof [];

    t.equal(Array.isArray(expected), Array.isArray(actual));
    t.end();
});

test('null case', function (t) {
    var actual = sumNum.sumElements([0]);
    var expected = 0;

    t.equal(actual, expected);
    t.end();
});

test('string', function (t) {
    var actual = typeof sumNum.sumElements(["apple"]);
    var expected = "string";

    t.equal(actual, expected);
    t.end()
});