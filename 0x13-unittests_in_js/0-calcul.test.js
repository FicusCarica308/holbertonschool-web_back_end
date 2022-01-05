// Tests for 0-calcul.js

const assert = require("assert");
const calculateNumber = require("./0-calcul.js");


describe("Round test", function() {
  it("checks if a and b are rounded and added together properly", function() {
    assert.equal(calculateNumber(1, 3), 4);
    assert.equal(calculateNumber(1, 3.7), 5);
    assert.equal(calculateNumber(1.2, 3.7), 5);
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });
});
