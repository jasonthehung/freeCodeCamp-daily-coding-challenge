function fibonacciSequence(startSequence, length) {
  if (startSequence.length >= length) {
    return startSequence.slice(0, length);
  }

  const result = [...startSequence];

  while (result.length < length) {
    const last = result[result.length - 1];
    const secondLast = result[result.length - 2];
    result.push(last + secondLast);
  }

  return result;
}
