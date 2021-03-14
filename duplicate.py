this_list = [1, 2, 4, 4, 5, 6 , 9, 10 , 11, 12 , 1]

def remove_duplicates(some_list):
    mylist= set(some_list)
    return [mylist]


print(remove_duplicates(this_list))
    
    
       
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)