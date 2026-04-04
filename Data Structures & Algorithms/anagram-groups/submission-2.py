class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countS = defaultdict(list) # to avoid key error
        
        for string in strs:
            count = [0] * 26 # a - z are 26 characters
            for c in string:
                # we wanna use ascii value as an index 
                # but we first need to bring them in range 0 to 26
                # e.g. ascii of a - ascii of a = 0
                # ascii of c - ascii of a = 2
                count[ord(c) - ord("a")] += 1
            countS[tuple(count)].append(string)
        
        return list(countS.values())
            