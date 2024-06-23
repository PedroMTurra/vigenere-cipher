from services.calculate_encoding import *
from services.convert_funcs import *
from services.equal_key_to_phrase import *

def listener_encode(
    phrase: str,
    key: str,
    alphabet: str,
) -> str:
    
    phrase, key = equal_key_to_phrase(phrase, key)
    phrase_in_num = convert_letter_to_num(phrase, alphabet)
    key_in_num = convert_letter_to_num(key, alphabet)
    final_nums = calculate_new_letter(phrase_in_num, key_in_num)
    final_phrase = convert_num_to_letter(final_nums, alphabet)
    
    return final_phrase