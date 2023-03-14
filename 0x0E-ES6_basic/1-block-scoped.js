export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    /* disable */
    task = true;
    task2 = false;
    /* enable */
  }

  return [task, task2];
}
