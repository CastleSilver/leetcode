class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        # DP 테이블 초기화
        dp = [[False] * n for _ in range(n)]
        
        start = 0
        max_length = 1

        # 길이 1인 팰린드롬
        for i in range(n):
            dp[i][i] = True

        # 길이 2인 팰린드롬
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2

        # 길이가 3 이상인 팰린드롬
        for length in range(3, n + 1):  # 부분 문자열의 길이
            for i in range(n - length + 1):
                j = i + length - 1  # 부분 문자열의 끝 인덱스

                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = length

        return s[start:start + max_length]
