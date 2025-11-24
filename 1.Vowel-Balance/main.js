function isBalanced(s) {
  const set = new Set("aeiouAEIOU");
  const n = s.length;
  const half = Math.floor(n / 2);

  let balance = 0;
  for (let i = 0; i < half; i++) {
    if (set.has(s[i])) balance++;
    if (set.has(s[n - i - 1])) balance--;
  }

  return balance === 0;
}
