export default function signUpUser(firstName, lastName) {
  return new Promise((resolve, reject) => {
    if (typeof firstName === 'string' && typeof lastName === 'string') {
      const user = { firstName, lastName };
      resolve(user);
    } else {
      reject(new Error('Invalid arguments: firstName and lastName must be strings'));
    }
  });
}
