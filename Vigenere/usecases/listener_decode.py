from services.calculate_decoding import *
from services.convert_funcs import *
from services.equal_key_to_phrase import *

def listener_decode(
    phrase: str,
    key: str,
    alphabet: str,
) -> str:
    
    phrase, key = equal_key_to_phrase(phrase, key)
    phrase_in_num = convert_letter_to_num(phrase, alphabet)
    key_in_num = convert_letter_to_num(key, alphabet)
    final_nums = decoding_calc(phrase_in_num, key_in_num)
    decoded_phrase = convert_num_to_letter(final_nums, alphabet)
    
    return decoded_phrase