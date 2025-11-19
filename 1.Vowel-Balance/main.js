function isBalanced(str) {
  const vowels = /[aeiou]/i;
  const n = str.length;
  const half = Math.floor(n / 2);

  let balance = 0;

  for (let i = 0; i < half; i++) {
    if (vowels.test(str[i])) balance++;
    if (vowels.test(str[n - 1 - i])) balance--;
  }

  return balance === 0;
}
