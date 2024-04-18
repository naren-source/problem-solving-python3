def printDuplicates(iStr: str) -> None:
    asciiLimit = 127
    mapList = [-1] * asciiLimit
    for x in iStr:
        mapList[ord(x)] += 1
    for x in iStr:
        if (not mapList[ord(x)] == -1) and mapList[ord(x)] > 0:
            mapList[ord(x)] = -1
            print(x, end=",")


printDuplicates(input())

# Write a program to print all the duplicates
#
# Input Format
#
# Input contains a string
#
# Constraints
#
# 1<=length<=1000
#
# Output Format
#
# Print the duplicates
#
# Sample Input 0
#
# hhVX6CmXBaP4JgjFSEFSrC5PNZYvSvxnbTJcD8RdWz8CQMv2PiGcxf5cR9GG2gMMqUvakegWU5YrvT7gvYk9FaEgMgatuvABAQBw
# Sample Output 0
#
# h,X,C,B,a,P,J,g,F,S,E,r,5,Y,v,x,T,c,8,R,W,Q,M,2,G,9,U,k,A,