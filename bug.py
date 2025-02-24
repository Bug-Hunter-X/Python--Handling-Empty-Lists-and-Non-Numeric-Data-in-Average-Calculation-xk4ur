def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}") #This will return 0 as expected

my_list_with_zero = [10, 0, 20]
result = calculate_average(my_list_with_zero)
print(f"The average is: {result}") #This will give the correct average which is 10

my_list_with_strings = [10, '20', 30]
result = calculate_average(my_list_with_strings) #This will cause a TypeError because of string and integer mix
print(f"The average is: {result}")