class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        L1 = len(s)
        L2 = len(t)
        if (L1 != L2):
            return False
        dictS = {}
        dictT = {}
        for c in s:
            dictS[c] = dictS.get(c, 0) + 1
        for c in t:
            dictT[c] = dictT.get(c, 0) + 1
        # check if all the value in s matches in t
        for keyS in dictS:
            valueS = dictS[keyS]
            valueT = dictT.get(keyS, 0) # if it doesn't exist, it would be zero
            if valueS != valueT:
                return False
        return True

        