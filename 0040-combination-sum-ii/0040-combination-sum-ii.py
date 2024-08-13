from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to handle duplicates and to improve efficiency
        ans = []
        self.backtrack(target, [], 0, candidates, ans)
        return ans
            
    def backtrack(self, target: int, path: List[int], curIdx: int, candidates: List[int], ans: List[List[int]]):
        if target == 0:
            ans.append(path[:])  # Use a copy of path
            return
        
        for i in range(curIdx, len(candidates)):
            # Skip duplicates
            if i > curIdx and candidates[i] == candidates[i - 1]:
                continue
            
            if candidates[i] > target:
                break  # No need to continue if the current number is greater than the remaining target
            
            # Include candidates[i] in the combination and move to the next index
            path.append(candidates[i])
            self.backtrack(target - candidates[i], path, i + 1, candidates, ans)
            path.pop()  # Backtrack, remove the last element to explore new possibilities
