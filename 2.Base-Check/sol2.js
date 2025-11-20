function isValidNumber(n, base) {
  if (base < 2 || base > 36) return false;

  const digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const allowedSet = new Set(digits.slice(0, base));

  const upperN = n.toUpperCase();

  for (const char of upperN) {
    if (!allowedSet.has(char)) return false;
  }

  return true;
}
