const chai = require("chai");
const expect = chai.expect;
// import sinon
const sinon = require("sinon");
// Request
const request = require('request');

describe('Index page', () => {
  it('returns status code 200', (done) => {
    request('http://localhost:7865', (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
