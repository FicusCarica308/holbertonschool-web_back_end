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
    sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(5.3, 3.7);
    expect(Utils.calculateNumber.calledOnce).to.be.true;
  });
});
