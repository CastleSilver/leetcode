class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        shift = min(arr)
        n = max(arr) - shift
        counts = [0]*(n+1)
        
        min_gap = inf
        counts[arr[0]-shift] = 1
        for i in range(1, len(arr)):
            min_gap = min(min_gap, abs(arr[i] - arr[i-1]))
            counts[arr[i]-shift] += 1
        
        ans = []
        for i in range(n + 1 - min_gap):
            if counts[i] > 0 and counts[i + min_gap] > 0:
                ans.append([i+shift, i+min_gap+shift])
        
        return ans