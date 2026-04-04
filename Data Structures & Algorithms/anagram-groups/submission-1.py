class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countS = defaultdict(list) # to avoid key error
        
        for string in strs:
            sortString = ''.join(sorted(string)) # use as a key
            countS[sortString].append(string) # append actual string
        
        return list(countS.values())



            