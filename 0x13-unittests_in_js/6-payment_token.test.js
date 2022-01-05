// Task(6) - tests for getPaymentTokenFromAPI()
const chai = require("chai");
const expect = chai.expect;
// import sinon
const sinon = require("sinon");
//import testing functions
const getPaymentTokenFromAPI = require('./6-payment_token.js');

describe('getPaymentTokenFromAPI', function() {
  it("Async test", function(done) {
    getPaymentTokenFromAPI(true)
    .then((res) => {
      expect(res).to.eql( {data: 'Successful response from the API'} );
      done();
    })
  });
});
