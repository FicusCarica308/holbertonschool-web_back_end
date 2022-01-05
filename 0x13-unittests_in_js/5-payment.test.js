// Task(3) - tests for sendPaymentRequestToApi()
const chai = require("chai");
const expect = chai.expect;
// import sinon
const sinon = require("sinon");
//import testing functions
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');

describe("sendPaymentRequestToApi", function() {
  let consoleSpy = NaN;
  beforeEach(function() {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(function() {
    sinon.restore();
  });

  it("Test console.log output for a = 100 and b = 20", function() {
    sendPaymentRequestToApi(100, 20);
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;
  });
  it("Test console.log output for a = 10 and b = 10", function() {
    sendPaymentRequestToApi(10, 10);
    expect(consoleSpy.calledWith('The total is: 20')).to.be.true;
  });
});
