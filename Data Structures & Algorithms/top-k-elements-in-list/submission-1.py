class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 ={}
        for key in nums:
            dict1[key] = dict1.get(key ,0 )+1
        def get_frequency(key): # take key 
            return dict1[key]   # return frequency
        sorted_nums =                 sorted(dict1.keys(),key=get_frequency,reverse=True)
        return sorted_nums[0:k]