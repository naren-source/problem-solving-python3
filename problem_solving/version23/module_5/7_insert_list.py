def shift_to_right(list_items, index):
    list_items += [None]
    for idx, _ in enumerate(list_items):
        if index != 0 and index == idx: break
        list_items[len(list_items) - 1 - idx] = \
            list_items[len(list_items) - 1 - (idx+1)]


def insert_to_list(list_items: list, insert: int) -> list:
    for idx, i in enumerate(list_items):
        if i >= insert or idx == (len(list_items)-1):
            if idx == (len(list_items)-1):
                list_items += [insert]
                break
            shift_to_right(list_items, idx)
            list_items[idx] = insert
            break
    return list_items


list_size = int(input())
input_list = [int(x) for x in input().split()]
insert_element = int(input())
return_list = insert_to_list(input_list, insert_element)
for i in return_list:
    print(i, end=" ")



#Write a program to insert an element in the array

# Input Format
#
# Input will be the size and the elements
#
# Constraints
#
# 1<=size<=1000
#
# Output Format
#
# Print the array
#
# Sample Input 0
#
# 10
# 1 5 18 28 33 39 47 73 77 84
# 37
# Sample Output 0
#
# 1 5 18 28 33 37 39 47 73 77 84