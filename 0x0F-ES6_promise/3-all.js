/* Task(3) */
import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const user = createUser();
  const photo = uploadPhoto();

  Promise.all([user, photo]).then((values) => {
    const data = { ...values[0], ...values[1] };
    console.log(data.body, data.firstName, data.lastName);
  }).catch(() => {
    console.log('Signup system offline');
  });
}
