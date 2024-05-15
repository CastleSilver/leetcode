class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ngDict = {}
        for i in range(len(nums2)):
            ngDict[nums2[i]] = -1
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    ngDict[nums2[i]] = nums2[j]
                    break
                    
        ans = []
        for i in range(len(nums1)):
            ans.append(ngDict[nums1[i]])
        return ans
            