def countStrTypes(iStr: str) -> None:
    vowels = ['a', 'e', 'i', 'o', 'u']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    vCount, cCount, dCount, sCount = [0, 0, 0, 0]
    for x in iStr:
        x = x.lower()
        if x in vowels:
            vCount += 1
        elif x in digits:
            dCount += 1
        elif x == " ":
            sCount += 1
        else:
            cCount += 1
    print(f"Vowels : {vCount}")
    print(f"Consonants : {cCount}")
    print(f"Digits : {dCount}")
    print(f"White spaces : {sCount}")


inputStr = input()
countStrTypes(inputStr)

# Write a program to count the number of vowels , consonants , digits and white spaces in the string
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
# Print the count
#
# Sample Input 0
#
# WkfcqZn  kytb JY3ZA48 34YPENF 3AruNa6J HzydUrS
# Sample Output 0
#
# Vowels : 6
# Consonants : 27
# Digits : 7
# White spaces : 6