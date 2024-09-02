class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ch_list = defaultdict(int)

        for s in magazine:
            ch_list[s] += 1
        
        for ch in ransomNote:
            ch_list[ch] -= 1
            if ch_list[ch] < 0:
                return False
        
        return True