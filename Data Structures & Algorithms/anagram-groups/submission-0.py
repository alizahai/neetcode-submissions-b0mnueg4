class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countS = {}
        
        for string in strs:
            sortString = ''.join(sorted(string)) # use as a key
            if sortString not in countS: # avoid key error
                countS[sortString] = []
            countS[sortString].append(string) # append actual string
        
        return list(countS.values())



            