#What is the Big O Notation?

def funChallenge(input):
    a = 10 #O(1)
    a = 50 + 3 #O(1)
    for i in input.length: #O(n)
        anotherFunction() #O(n)
        stranger = True #O(n)
        a+=1 #O(n)
    return a #O(1)

#Big O(3 + 4n) or Big O(n)