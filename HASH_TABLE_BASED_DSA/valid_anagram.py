# https://leetcode.com/problems/valid-anagram/description/

def validAnagram(s,t):
    countT,countS = {},{}

    for index in range(t):
        countT[t[index]] =  1 + countT.get(t[index],0)
    for index in range(s):
        countS[s[index]] = 1 + countS.get(s[index],0)


    for letter, count in countT.items():
        if countT[letter] != countS.get(letter,0):
            return False
    return True    
              
        


    # countA, countB = {}, {}

    # for index in range(len(s)):
    #     countA[s[index]] = 1 + countA.get(s[index],0)

    # for index in range(len(t)):
    #     countB[t[index]] = 1 + countB.get(t[index],0)

    # for c in countA.items():
    #     if countA[c[0]] != countB.get(c[0],0):
    #         return False
    # return True


print(validAnagram("anagram","nagaram"))
print(validAnagram("rat","car"))

    