def jbelmu(text):
    return " ".join(
        w if len(w) < 2 else f"{w[0]}{''.join(sorted(w[1:-1]))}{w[-1]}"
        for w in text.split()
    )