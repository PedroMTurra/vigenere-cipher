from usecases.listener_convert_phrase import *
from usecases.listener_decode import *

def encode_or_decode(
    phrase: str,
    key: str,
    alphabet: str,
):
    
    choice = input("Encode [1] or Decode [2] -> ")
    
    if choice == "1":
        final = listener_encode(phrase, key, alphabet)
    elif choice == "2":
        final = listener_decode(phrase, key, alphabet)
        
    print(final)