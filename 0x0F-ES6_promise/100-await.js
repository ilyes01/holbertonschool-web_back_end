import { uploadPhoto, createUser } from "./utils";

export default async function asyncUploadUser() {
  let photo, user;
  try {
    photo = await uploadPhoto();
    user = await createUser();
    return { photo, user };
  } catch (error) {
    return { photo: null, user: null };
  }
}
