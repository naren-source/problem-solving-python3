# # list
# l = ["bob", "rolf", "anne"]
# print(l)
# print(l[0])
# l[1] = "newName"
# print(l)
# l.append("helloww")
# print(l)
# l.remove("anne")
# # tuple
# t = ("bob", "rofl", "anne")
# print(t)
# print(t[2])
# # t[2] = "ahh"
# # print(t)
#
# # set
# s = {"bob", "folr", "anne"}
# print(s)
# s.add("follow")
# print(s)
# s.remove("folr")
# print(s)


#More on sets
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local_friends = friends.difference(abroad)
print(local_friends)
un_local_friends = abroad.difference(friends)
print(un_local_friends)

local = {"Rolf"}
abroad = {"bob", "chan"}
total = local.union(abroad)
print(total)

arts = {"a", "b", "c", "d"}
science = {"a", "b", "e", "f"}
total = arts.intersection(science)
print(total)
