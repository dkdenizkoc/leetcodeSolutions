class Solution:
    def mergeAlternately(word1: str, word2: str) -> str:
        lenW1 = len(word1)
        lenW2 = len(word2)
        iW1 = 0
        iW2 = 0
        lenTotal = lenW1 + lenW2
        iTotal = 0
        newString = ""
        while iTotal < lenTotal:
            if(iW1 + 1 <= lenW1):
                newString += word1[iW1]
                iW1 += 1
                iTotal += 1
                print("iW1 : ",iW1)
            if(iW2 + 1 <= lenW2 and iTotal < lenTotal):
                newString += word2[iW2]
                iW2 += 1
                iTotal +=1
                print("iW2 : ",iW2)
                
            print(iTotal)
        return newString


print(Solution.mergeAlternately("abc","xyz"))