group_of_people = ['Alex', 'Eliot', 'Veronica', 'Lucy', 'Wouter', 'Bart']

# using comprehension
names_with_four_letters = [name for name in group_of_people if len(name) == 4]
print(names_with_four_letters)

# using for loop needs more lines of coding
other_list_of_names_with_four_letters = []
for name in group_of_people:
    if len(name) == 4:
        other_list_of_names_with_four_letters.append(name)
print(other_list_of_names_with_four_letters)
