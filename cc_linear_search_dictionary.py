def linear_search_dictionary(the_dictionary, target):
    for key, value in the_dictionary.items():
        if value == target:
            print(f"Found at key {key}!")
            return value
    print("Target is not in the dictionary!")
    return -1


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)

