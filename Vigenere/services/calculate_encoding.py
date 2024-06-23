def calculate_new_letter(
    phrase_nums: list, 
    key_nums: list,
) -> list:
    
    final_num_list = []
    
    for idx in range(0, len(phrase_nums)):
        
        num1 = phrase_nums[idx]
        num2 = key_nums[idx]
        new_num = num1 + num2
        
        if new_num > 25:
            new_num -= 26
        
        final_num_list.append(new_num)
        
    return final_num_list