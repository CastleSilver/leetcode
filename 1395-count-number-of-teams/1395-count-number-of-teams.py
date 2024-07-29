from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        
        for i in range(n):
            less_left = less_right = more_left = more_right = 0
            
            for j in range(n):
                if j < i:
                    if rating[j] < rating[i]:
                        less_left += 1
                    if rating[j] > rating[i]:
                        more_left += 1
                elif j > i:
                    if rating[j] < rating[i]:
                        less_right += 1
                    if rating[j] > rating[i]:
                        more_right += 1
            
            ans += less_left * more_right + more_left * less_right
        
        return ans