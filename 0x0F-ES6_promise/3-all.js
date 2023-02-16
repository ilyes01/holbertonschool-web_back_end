import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  try {
    const [photoResponse, user] = await Promise.all([uploadPhoto(), createUser()]);
    const { body: photoUrl } = photoResponse;
    const { firstName, lastName } = user;
    console.log(`${photoUrl} ${firstName} ${lastName}`);
  } catch (error) {
    console.log('Signup system offline');
  }
}
