def space_jam(s):
    no_space = "".join(s.split())

    upper = no_space.upper()

    result = "  ".join(upper)
    
    return result