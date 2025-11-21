function spaceJam(s: string) {
  const noSpace = s.replace(/\s+/g, "");

  const upper = noSpace.toUpperCase();

  return upper.split("").join("  ");
}
