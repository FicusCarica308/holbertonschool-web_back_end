import { createQueue } from 'kue';

const queue = createQueue();
const jobTemplate = {
    phoneNumber: '(xxx)-xxx-xxxx',
    message: 'Test message',
}

var job = queue.create('push_notification_code', jobTemplate).save((err) => {
  if( !err ) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', (res) => {
  console.log('Notification job completed');
}).on('failed', (err) => {
  console.log('Notification job failed')
})
