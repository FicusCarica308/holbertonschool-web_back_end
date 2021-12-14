/* Task(6) */
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)]).then(
    (values) => {
      const data = values;
      for (const settlement of data) {
        if (settlement.reason) {
          settlement.value = settlement.reason.toString();
          delete settlement.reason;
        }
      }
      return (data);
    },
  );
}
