class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        str_dict = {}
        for i in range(len(arr)):
            str_dict[arr[i]] = str_dict.get(arr[i], 0) + 1
        
        for key in str_dict:
            if str_dict.get(key, 0) == 1:
                k -= 1
                if k == 0:
                    return key
        return ""