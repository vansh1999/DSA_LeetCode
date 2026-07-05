
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # to iterate all words
        A , B = len(word1) , len(word2)
        # pointer like i or j at each word
        a,b = 0,0
        # will create new word array, not using string, as str in py is immutable and requires O(n) each time
        word_merge = []
        # will you one pointer to refer and append to word 1 or word 2 altenatively
        word = 1


        while a < A and b < B:

            if word == 1:
                word_merge.append(word1[a])
                a = a+1
                word = 2
            else:
                word_merge.append(word2[b])
                b = b+1
                word = 1

        # when B ends and only A chars are left
        while a < A:
            word_merge.append(word1[a])
            a = a + 1
        
        # when A ends and only B chars are left
        while b < B:
            word_merge.append(word2[b])
            b = b + 1
    
        return ''.join(word_merge)

sol = Solution()
print(sol.mergeAlternately("abc" , "defgh"))



### more single , but using str

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:

        # i = 0
        # merge_word = ""

        # while i < len(word1) or i < len(word2):
        #     if i < len(word1):
        #         merge_word = merge_word + word1[i]
        #     if i < len(word2):
        #         merge_word = merge_word + word2[i]
        #     i = i + 1
        # return merge_word


# sol = Solution()
# print(sol.mergeAlternately("abc" , "defgh"))
