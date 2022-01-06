// Tests for 0-calcul.js

const assert = require("assert");
const calculateNumber = require("./1-calcul.js");


describe("calculateNumber", function() {
  it("tests 'SUM' functionality of calculateNumber", function() {
    assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  it("tests 'SUBTRACT' functionality of calculateNumber", function() {
    assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });
  it("tests 'DIVIDE' functionality of calculateNumber", function() {
    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });
  it("tests 'DIVIDE' functionality of calculateNumber returns 'Error'", function() {
    assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
