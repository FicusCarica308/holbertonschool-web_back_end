const chai = require("chai");
const expect = chai.expect;
// import sinon
const sinon = require("sinon");
// Request
const request = require('request');

describe('Index page', () => {
  it('returns status code 200 & proper body for root', (done) => {
    request('http://localhost:7865', (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('returns status code 200 for valid id (/cart/:id)', (done) => {
    request('http://localhost:7865/cart/12', (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('returns status code 404 for invalid id (/cart/:id)', (done) => {
    request('http://localhost:7865/cart/invalid', (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
