friends = ["aa", "ab", "bc", "bb"]
newList = []

#usual way
# for frnd in friends:
#     if frnd.startswith("a"):
#         newList.append(frnd)

#Using list comprehension

newList = [f for f in friends if f[0].lower() == "a"]

print(newList)
print(id(newList))
