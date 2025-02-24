def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}")

my_list_with_zero = [10, 0, 20]
result = calculate_average(my_list_with_zero)
print(f"The average is: {result}")

my_list_with_strings = [10, '20', 30]
result = calculate_average(my_list_with_strings)
print(f"The average is: {result}") #This will return 20 because it ignores the string

my_list_with_only_strings = ['a','b','c']
result = calculate_average(my_list_with_only_strings)
print(f"The average is: {result}") #This will return 0