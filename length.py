
#Write a Python program to find the list of words that are longer than n from a given list of words.
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "The quick brown fox jumps over the lazy dog"))

#Write a Python function that takes two lists and returns True if they have at least one common member.


def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))  # since there are two list to iterate, two for loop
print(common_data([1,2,3,4,5], [6,7,8,9]))

def count_common(list1, list2):
     common = []
     for x in list1:
         for y in list2:
             if x == y:
                common.append(x)
     return common
print(count_common([1,2,3,4,5,6, 7, 8], [5,6,7,8,9]))  # since there are two list to iterate, two for loop
print(count_common([1,2,3,4,5], [6,7,8,9]))


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color1 = [item for (i,item) in enumerate(color) if i not in (0,4,5)]   # i = insdex, x is  the item
print(color1)


print([item for (index, item) in enumerate(color) if index not in (0,4, 5)])


#closest to ZERO
def takeClosest(myList, myNumber):
    closest = myList[0]
    for i in range(1, len(myList)):
        if abs(i - myNumber) < closest:
            closest = i
    return closest


#Write a Python program to generate a 3*4*6 3D array whose each element is *.   ( 6, 4, 3)
#array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
#print(array)


s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)

#Find the index of an item in a specified list
num =[10, 30, 4, -6]

print(num.index(30))

import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))                            # random.choice




