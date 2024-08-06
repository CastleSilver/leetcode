class Solution:
    def minimumPushes(self, word: str) -> int:
    
        cnt_map = {}
        for str in word:
            cnt_map[str] = cnt_map.get(str, 0) + 1
        
        cnt_map = sorted(cnt_map.items(), reverse=True, key=lambda x:x[1])
        keypad = 0
        ans = 0
        for key, value in cnt_map:
            ans += value * ((keypad//8) + 1)
            keypad += 1
        return ans