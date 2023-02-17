export default function guardrail(mathFunction) {
  const queue = [];
  let result;
  try {
    result = mathFunction();
  } catch (e) {
    result = e.toString();
  } finally {
    queue.push(result);
    queue.push('Guardrail was processed');
  }
  return queue;
}
