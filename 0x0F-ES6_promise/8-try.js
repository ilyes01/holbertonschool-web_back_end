export default function divideFunction(numerator, denominator) {
  return new Promise((resolve, reject) => {
    if (denominator === 0) {
      reject(new Error('Cannot divide by zero'));
    } else {
      resolve(numerator / denominator);
    }
  });
}
