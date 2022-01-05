// Task(3) - tests for sendPaymentRequestToApi()
const chai = require("chai");
const expect = chai.expect;
// import sinon
const sinon = require("sinon");
//import testing functions
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');

describe("sendPaymentRequestToApi", function() {
  it("spy test", function() {
    const consoleSpy = sinon.spy(console, 'log');
    const calculateNumberStub = sinon.stub(Utils, `calculateNumber`).returns(10);
    sendPaymentRequestToApi(100, 20);
    expect(calculateNumberStub.calledOnceWith('SUM', 100, 20)).to.be.true;
    
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;
  });
});
