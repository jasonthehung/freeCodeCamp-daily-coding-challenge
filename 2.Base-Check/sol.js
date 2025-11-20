function isValidNumber(n, base) {
  if (base < 2 || base > 36) return false;

  const digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const allowed = digits.slice(0, base);
  const re = new RegExp(`^[${allowed}]+$`, "i");

  return re.test(n);
}
