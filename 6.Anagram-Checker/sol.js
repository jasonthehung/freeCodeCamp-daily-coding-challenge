function areAnagrams(str1, str2) {
	const s1 = str1.replace(/\s+/g, "").toLowerCase()
	const s2 = str2.replace(/\s+/g, "").toLowerCase()

	if (s1.length !== s2.length) return false

	const charCount = {}

	for (const char of s1) {
		charCount[char] = (charCount[char] || 0) + 1
	}

	for (const char of s2) {
		if (!charCount[char]) return false
		charCount[char] -= 1
	}

	return true
}
