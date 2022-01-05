// Tests for 0-calcul.js

const assert = require("assert");
const { expect } = require("chai");
const calculateNumber = require("./1-calcul.js");


describe("calculateNumber", function() {
  it("tests 'SUM' functionality of calculateNumber", function() {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  it("tests 'SUBTRACT' functionality of calculateNumber", function() {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
  it("tests 'DIVIDE' functionality of calculateNumber", function() {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
  it("tests 'DIVIDE' functionality of calculateNumber returns 'Error'", function() {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });
});
