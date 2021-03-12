# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)


# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)



# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]


def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]  # if same,  young age should come first
    age = item[2]
    return (error, age)


sorted_list = sorted(participant_list, key=sorter)
print(sorted_list)
