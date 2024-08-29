class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        temp = []
        temp_len = 0

        for word in words:
            # If adding this word exceeds the maxWidth, we need to justify the current line
            if temp_len + len(temp) + len(word) > maxWidth:
                space = maxWidth - temp_len  # Total space to distribute
                if len(temp) == 1:  # If there's only one word, left-justify it
                    ans.append(temp[0] + ' ' * space)
                else:
                    spaces_per_gap = space // (len(temp) - 1)
                    extra_spaces = space % (len(temp) - 1)
                    
                    for i in range(extra_spaces):
                        temp[i] += ' '  # Distribute the extra spaces
                        
                    ans.append((' ' * spaces_per_gap).join(temp))  # Join words with evenly distributed spaces
                
                # Reset temp and temp_len for the next line
                temp, temp_len = [], 0
            
            # Add the current word to the temp list
            temp.append(word)
            temp_len += len(word)

        # Handle the last line (left-justified)
        last_line = ' '.join(temp)
        last_line += ' ' * (maxWidth - len(last_line))
        ans.append(last_line)

        return ans
