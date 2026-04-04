class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        # delimeter: length of each string + #
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        
        return encoded_string
    
    def decode(self, s: str) -> List[str]:
        strs, i = [], 0

        # iterate over each word
        while i < len(s):
            j = i
            # increment j while we still are at integer portion at beginning of #
            while s[j] != "#":
                j += 1
            # length of string : integer before #
            length = int(s[i:j])
            # append word to list starting from one position next to # till the length of word
            strs.append(s[j + 1 : j + 1 + length])
            # i : starting index of next word
            i = j + 1 + length
        
        return strs
