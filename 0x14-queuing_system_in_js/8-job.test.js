const assert = require("assert");
const chai = require("chai");
const expect = chai.expect; 
const kue = require('kue');
const createPushNotificationsJobs = require('./8-job.js');

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(function() {
    queue.testMode.enter(true);
  });
 after(function() {
    queue.testMode.exit()
  }); 
  it('display a error message if jobs is not an array', () => {
    assert.throws(() => { createPushNotificationsJobs(1, queue) }, Error, 'Jobs is not an array');
  });
  it('creates more than one job at once', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 1235 to verify your account'
      }
    ];
    try {
      createPushNotificationsJobs(list, queue);
    } catch {
      expect(queue.testMode.jobs.length).to.equal(2);
    }
  });
});
