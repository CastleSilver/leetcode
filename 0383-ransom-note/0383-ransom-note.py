class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False

        ch_list = defaultdict(int)

        for s in magazine:
            ch_list[s] += 1
        
        for ch in ransomNote:
            if ch_list[ch] <= 0:
                return False
            ch_list[ch] -= 1
        
        return True