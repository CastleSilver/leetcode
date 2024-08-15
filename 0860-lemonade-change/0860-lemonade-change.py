class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False

        #Count bills I have
        cnt = [0, 0, 0]

        for bill in bills:
            if bill == 5:
                cnt[0] += 1
            if bill == 10:
                cnt[1] += 1
                if cnt[0] <= 0:
                    return False
                else:
                    cnt[0] -= 1
            if bill == 20:
                cnt[2] += 1
                if cnt[1] >= 1 and cnt[0] >= 1:
                    cnt[1] -= 1
                    cnt[0] -= 1
                elif cnt[0] >= 3:
                    cnt[0] -= 3
                else:
                    return False
        
        return True