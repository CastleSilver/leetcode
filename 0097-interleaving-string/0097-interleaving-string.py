class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # s1과 s2의 길이 합이 s3의 길이와 다르면 간섭할 수 없음
        if len(s1) + len(s2) != len(s3):
            return False
        
        # DP 테이블 초기화
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True  # 기본 초기화
        
        # 첫 번째 열 초기화: s1의 첫 i개 문자만으로 s3의 첫 i개 문자를 구성할 수 있는지
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        # 첫 번째 행 초기화: s2의 첫 j개 문자만으로 s3의 첫 j개 문자를 구성할 수 있는지
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        # DP 테이블 채우기
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        # 결과 반환
        return dp[len(s1)][len(s2)]
