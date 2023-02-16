export default function handleResponseFromAPI(promise) {
  const successResponse = { status: 200, body: 'success' };
  const errorResponse = new Error();
  const logResponse = () => console.log('Got a response from the API');

  return promise
    .then(() => successResponse)
    .catch(() => errorResponse)
    .finally(logResponse);
}

