export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    /* disable */
    const task = true;
    const task2 = false;
    /* enable */
  }

  return [task, task2];
}
