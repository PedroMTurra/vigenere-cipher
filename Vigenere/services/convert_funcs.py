def convert_letter_to_num(
    phrase: str, 
    alphabet: str
) -> list:
    
    converted_phrase = []
    
    for letter in phrase:
        num = alphabet.index(letter)
        converted_phrase.append(num)
        
    return converted_phrase
        
def convert_num_to_letter(
    num_list: list,
    alphabet: str
) -> str:
    
    final_phrase = []
    
    for num in num_list:
        letter = alphabet[num]
        final_phrase.append(letter)
        
    return str("".join(final_phrase))