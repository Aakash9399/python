def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_num = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and roman_dict[s[i:i+2]] > roman_dict[s[i]]:
            int_num += roman_dict[s[i:i+2]]
            i += 2
        else:
            int_num += roman_dict[s[i]]
            i += 1

    return int_num
print(roman_to_int('IV'))