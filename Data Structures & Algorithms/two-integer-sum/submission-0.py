class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums = [2,7,11,15] 
        #target =17
        i=0 
        size = len(nums)
        #print(size) # 4
        while(i<size) :
            j=i+1
            while(j<size) :
                    if nums[i] +nums[j] == target :
                        
                        return [i ,j]
                    j=j+1
            i=i+1