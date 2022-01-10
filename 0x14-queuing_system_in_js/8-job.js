export default function createPushNotificationsJobs(jobs, queue) {
  if (!jobs instanceof Array) {
    throw new Error('Jobs is not an array');
  }
  for (const jobData of jobs) {
    const newJob = queue.create('push_notification_code_2', jobData).save((err) => {
      if(!err) {
        console.log(`Notification job created: ${newJob.id}`);
      }
      newJob.on('complete', (res) => {
        console.log(`Notification job #${newJob.id} completed`);
      }).on('failed', (err) => {
        console.log(`Notification job #${newJob.id} failed: ${err}`)
      }).on('progress', (progress) => {
        console.log(`Notification job #${newJob.id} ${progress}% complete`)
      });
    });
  }
}
