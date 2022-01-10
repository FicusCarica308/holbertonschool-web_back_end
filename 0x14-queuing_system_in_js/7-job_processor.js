import { createQueue } from 'kue';
import { jobs } from 'kue/lib/queue/test_mode';

const blacklisted = ['4153518780', '4153518781']
const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklisted.includes(phoneNumber)) {
    return done(`Phone number ${phoneNumber} is blacklisted`);
  }
  job.progress(50, 100)
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code_2', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
