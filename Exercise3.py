def count_letters(input_string):
    letter_counts = {}

    for char in input_string:
        if char.isalpha() and char.islower():
            letter_counts[char] = letter_counts.get(char, 0) + 1

    return letter_counts

user_input = input("Enter a string: ")

result_dict = count_letters(user_input)

print(result_dict)
