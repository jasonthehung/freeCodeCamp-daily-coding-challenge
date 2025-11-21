function jbelmu(text) {
  return text
    .split(" ")
    .map((w) =>
      w.length < 2
        ? w
        : `${w[0]}${[...w.slice(1, -1)].sort().join("")}${w[w.length - 1]}`
    )
    .join(" ");
}
