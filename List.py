# Sum
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
#print(sum_list([1,2,-8]))


#max
def max_num_in_list( list ):
    max = list[ 0 ]               # initialize 1st item as the max
    for a in list:
        if a > max:
            max = a
    return max
#print(max_num_in_list([1, 2, -8, 0]))

# Count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
#                                                       len(word> 1) and word[0] = word[-1]

def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]: # first and last same
      ctr += 1
  return ctr

#print(match_words(['abc', 'xyz', 'aba', '1221']))


#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#Sample List: [ (2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


def sorter(item): return item[-1]   # on Basis of key= last ko tuple ko digit vanera pathako ho

def sort_list_last(tuples):
  return sorted( tuples, key=sorter)                         # key
print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1, 0)]))


#Python lists have a built-in list.sort() method that modifies the list in-place. 
# There is also a sorted() built-in function that builds a new sorted list from an iterable.

#sorted(iterable, key=None, reverse=False)

#sorted(iterable, key = , reverse=True)


print(sorted([5, 2, 4, 1, 3], reverse=True ))


 
def try_making_sort():
# take the second element for sort
    def take_second(elem):
        return elem[1]


    # random list
    random = [(2, 2), (3, 4), (4, 1), (1, 3)]

    # sort list with key
    sorted_list = sorted(random, key=take_second)
    return sorted_list


#print('Sorted list:', try_making_sort())


def participant_list_filt():
# List elements: (Student's Name, Marks out of 100 , Age)
    participant_list = [
        ('Alison', 50, 18),
        ('Terence', 75, 12),
        ('David', 75, 20),
        ('Jimmy', 90, 22),
        ('John', 45, 12)
    ]


    def sorter(item):
        # Since highest marks first, highest = 100- obtained marks
        highest = 100 - item[1]                         # ani item [1 ] vanera ni garna parxa
        
        age = item[2]                           # if mathi ko same vayo vani, yo factor play ma aauxa jsto 6 but not sure
        return (highest, age)


    sorted_list = sorted(participant_list, key=sorter)

    return sorted_list

print(participant_list_filt())


