class Solution(object):
    def longestPalindrome(self, words):
        word_dict= {}
        answer = 0 
        for word in words:
            reverse= word[1]+word[0]

            if reverse in word_dict:
                word_dict[reverse] -=1
                if word_dict[reverse] == 0:
                    del word_dict[reverse] 
                answer += 4
            else:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
            
        for key in word_dict:
            if key[0] == key[1]:
                answer += 2
                break
        return answer
