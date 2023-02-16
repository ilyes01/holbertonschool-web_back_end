export default function uploadPhoto(fileName) {
  const errorMessage = `${fileName} cannot be processed`;
  return new Promise((resolve, reject) => {
    reject(new Error(errorMessage));
  });
}
