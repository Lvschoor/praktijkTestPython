my_data = ['My little text', 3.1415, 17, True]

numbers = list(range(2, 1001, 2))

print(numbers)

different_list = list('test')  # from string
another_list = list(('a', 'e', 'i', 'u'))  # from tuple
copied_list = another_list.copy()  # using copy()

print(type(different_list))
print(type(another_list))
print(type(copied_list))
