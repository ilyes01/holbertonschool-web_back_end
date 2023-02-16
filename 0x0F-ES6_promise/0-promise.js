export default function getResponseFromAPI() {
  const successResponse = 'Success';
  const errorResponse = new Error('API call failed');

  return new Promise((resolve, reject) => {
    const success = true;
    if (success) {
      resolve(successResponse);
    } else {
      reject(errorResponse);
    }
  });
}

