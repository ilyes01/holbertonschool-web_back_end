import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let photoPromise = uploadPhoto();
  let userPromise = createUser();

  try {
    const [photo, user] = await Promise.all([photoPromise, userPromise]);
    return { photo, user };
  } catch (error) {
    return { photo: null, user: null };
  }
}
