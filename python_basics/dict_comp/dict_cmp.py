users = [
    (0, "Bob", "pass"),
    (1, "Bob1", "pass"),
    (2, "Bob2", "pass"),
    (3, "Bob3", "pass")
]

username_mapping = {x[1]: x for x in users}

print(username_mapping)

u_inp = input("Username \n")
p_inp = input("Password \n")
_, uname, passw = username_mapping[u_inp]

if passw == p_inp:
    print("Success")
else:
    print("Fail")
