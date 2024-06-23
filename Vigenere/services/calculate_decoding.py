def decoding_calc(
    cript_phrase: str,
    key: str,
) -> list:
    
    cript_phrase = list(cript_phrase)
    key = list(key)
    
    num_list = []
    
    for idx in range(0, len(cript_phrase)):
        num1 = cript_phrase[idx]
        num2 = key[idx]
        new_num = (num1 - num2) + 26
        
        if new_num > 25:
            new_num -= 26
        
        num_list.append(new_num)
        
    return num_list