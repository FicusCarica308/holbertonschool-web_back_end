import { createQueue } from 'kue';

const queue = createQueue();
const jobTemplate = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
}

const job = queue.create('push_notification_code', jobTemplate).save((err) => {
  if( !err ) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', (res) => {
  console.log('Notification job completed');
}).on('failed', (err) => {
  console.log('Notification job failed')
})
