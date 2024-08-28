def swapCase(iStr: str) -> None:
    for x in iStr:
        if x.islower():
            print(x.upper(), end="")
        else:
            print(x.lower(), end="")


inputStr = input()
swapCase(inputStr)


# Write a program to toggle cases of each character of a string
#
# Input Format
#
# Given a string
#
# Constraints
#
# 1<=length<=1000
#
# Output Format
#
# Print the altered string
#
# Sample Input 0
#
# hhGHgCmcnrLXaPSSWiASENiPVajBGuUAVSyzUAPh
# Sample Output 0
#
# HHghGcMCNRlxApsswIasenIpvAJbgUuavsYZuapH