class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # DP 테이블 초기화
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case 초기화
        for i in range(1, m + 1):
            dp[i][0] = i  # word1의 첫 i개 문자를 삭제
        for j in range(1, n + 1):
            dp[0][j] = j  # word2의 첫 j개 문자를 삽입
        
        # DP 테이블 채우기
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]  # 문자가 같다면 편집 없이 그대로
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + 1,    # 삭제
                        dp[i][j-1] + 1,    # 삽입
                        dp[i-1][j-1] + 1   # 교체
                    )
        
        return dp[m][n]

        