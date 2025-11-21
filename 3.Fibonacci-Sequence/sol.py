def fibonacci_sequence(start_sequence, length):
    if len(start_sequence) >= length:
        return start_sequence[:length]
    
    result = start_sequence[:]

    while len(result) < length:
        index = len(result)
        last = result[index - 1]
        secondLast = result[index - 2]
        result.append(last + secondLast)

    return result