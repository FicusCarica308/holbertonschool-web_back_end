// Tests for 0-calcul.js

const assert = require("assert");
const calculateNumber = require("./0-calcul.js");


describe("calculateNumber", function() {
  it("checks if numbers are rounded and added together properly using integers", function() {
    assert.equal(calculateNumber(1, 3), 4);
  });
  it("checks if decimal numbers are rounded and added together properly", function() {
    assert.equal(calculateNumber(1, 3.7), 5);
    assert.equal(calculateNumber(1.2, 3.7), 5);
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });
  it("checks if negative numbers are rounded and added together properly", function() {
    assert.equal(calculateNumber(-1.2, -3.7), -5);
    assert.equal(calculateNumber(-3, -6), -9);
  });
});
