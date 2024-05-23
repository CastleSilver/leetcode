class Solution:
     def sortSentence(self, s: str) -> str:

        words = s.split()
        
        sorted_words = [""] * len(words)
        
        for word in words:
            position = int(word[-1]) - 1 

            sorted_words[position] = word[:-1]
        

        return " ".join(sorted_words)