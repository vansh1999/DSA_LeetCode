class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # also need to check no of elements in magazine to fulfill ransomNote

        # step 1 -> need unique letters and their values

        # build a counter -> use -> hashmap -> dict

        counter = {}

        for c in magazine:
            if c in counter:
                counter[c] = counter[c] + 1
            else:
                counter[c] = 1
        
        # or counter = Counter(magazine) 
        # from collections import Counter


        # now check each ransomNote exits in mag and keep deleting each occurance and if only 1 is left del it and if ransomNote is compete and mag is left, means yes we can construct -> true

        for note in ransomNote:
            if note not in counter:
                return False
            elif counter[note] == 1:
                del counter[note] 
            else:
                counter[note] = counter[note] - 1
        
        return True

