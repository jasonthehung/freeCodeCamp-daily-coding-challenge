function spaceJam(s) {
  const noSpaces = s.replace(/\s+/g, "");

  const upper = noSpaces.toUpperCase();

  return upper.split("").join("  ");
}
