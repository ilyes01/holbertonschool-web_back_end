// This function takes a numerator and a denominator and returns their quotient.
// If the denominator is 0, an error is thrown.

export default function divideFunction(numerator, denominator) {
  // Check if the denominator is 0.
  if (denominator === 0) {
    // If the denominator is 0, throw an error with the message "cannot divide by 0".
    throw Error('cannot divide by 0');
  }
  // If the denominator is not 0, return the quotient of the numerator and denominator.
  return numerator / denominator;
}
