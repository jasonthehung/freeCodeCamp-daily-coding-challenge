function areAnagrams(str1: string, str2: string) {
	const s1 = str1.toLowerCase().replace(/\s+/g, "")
	const s2 = str2.toLowerCase().replace(/\s+/g, "")

	if (s1.length !== s2.length) return false

	const map = new Map()
	for (const ch of s1) {
		map.set(ch, (map.get(ch) || 0) + 1)
	}

	for (const ch of s2) {
		if (!map.has(ch)) return false
		map.set(ch, map.get(ch) - 1)
		if (map.get(ch) < 0) return false
	}

	return true
}
