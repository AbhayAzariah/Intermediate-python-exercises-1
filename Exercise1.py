def get_unique_list(input_list):
    unique_set = set(input_list)

    unique_list = list(unique_set)

    return unique_list

my_list = [1, 2, 3, 2, 1, 4,4,4,4,4,4]
unique_list = get_unique_list(my_list)

print(unique_list)
