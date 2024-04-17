friends_ages = {
    "rolf": 24,
    "adam": 30,
    "Anne": 27
}

print(f"Rolf details: {friends_ages['rolf']}")

friends_ages['rolf'] = 30

print(f"Rolf details: {friends_ages['rolf']}")

friends = [
    {"name": "rolf"},
    {"name": "rolfie"}
]
print(friends[1]["name"])

stud_att = {"rolf": 12, "adam": 23}

for s in stud_att:
    print(f"{s} :  {stud_att[s]}")

for k, v in stud_att.items():
    print(f"{k} :  {v}")

if "rolzf" in stud_att:
    print("Yes")

values = stud_att.values()
print(values)
