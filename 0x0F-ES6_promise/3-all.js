/* Task(3) */
import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([createUser(), uploadPhoto()]).then((values) => {
    const data = { ...values[0], ...values[1] };
    console.log(`${data.body} ${data.firstName} ${data.lastName}`);
  }).catch(() => {
    console.log('Signup system offline');
  });
}
