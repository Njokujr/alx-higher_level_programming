#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return total

    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    total = 0
    i = 0

    while i in range(len(roman_string)):

        if i == len(roman_string) - 1:
            total += roman_dictionary[roman_string[i]]
            break

        else:
            if roman_dictionary[roman_string[i]] < roman_dictionary[roman_string[i+1]]:
                total += roman_dictionary[roman_string[i+1]] - roman_dictionary[roman_string[i]]
                i = i + 1

                if i + 1 == len(roman_string):
                    break

            else:
                total += roman_dictionary[roman_string[i]]

        i = i + 1

    return total
