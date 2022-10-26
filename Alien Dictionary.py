class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # put the order into a hash map: key = character, index = value
        orderInd = {c:i for i, c in enumerate(order)}

        # make sure words are lower case:
        words = [word.lower() for word in words]

        # loop through index minus 1: to compare every pair of words:
        for i in range(len(words)-1):
            # set w1 to index 0 of words and w2 to index 1 of words:
            w1, w2 = words[i], words[i+1]

            # for the characters in the length of w1:
            for j in range(len(w1)):
                # if the characters length in w1 == character length in w2: return false
                if j == len(w2):
                    # return False:
                    return False
                # elif the characters don't match: then check if sorted in correct order
                elif w1[j] != w2[j]:
                    # then check the value based on w2[j] and w1[j] as your keys in the orderInd dictionary:
                    if orderInd[w2[j]] < orderInd[w1[j]]:
                        return False
                    # break from loop:
                    break
        # return True:
        return True