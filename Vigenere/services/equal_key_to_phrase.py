def equal_key_to_phrase(phrase: str, key: str) -> str:
    
    phrase = list(phrase)
    key = list(key)
    
    diff = len(phrase) - len(key)
    
    if diff >= 0:
        for idx in range(0, diff + 1):
            letter = key[idx]
            key.append(letter)
    else:
        for idx in range(0, diff + 1):
            key.pop()
        
    phrase = str("".join(phrase))    
    key = str("".join(key))
    
    return phrase, key