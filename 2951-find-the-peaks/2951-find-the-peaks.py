class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        ans = []
        pre = mountain[0]
        flag = False
        for i in range(1, len(mountain)):
            if flag == False and mountain[i] > pre:
                flag = True
              
            elif flag:
                if mountain[i] < pre:
                    ans.append(i-1)
                    flag = False
                   
                elif mountain[i] == pre:
                    flag = False
    
            pre = mountain[i]
        return ans