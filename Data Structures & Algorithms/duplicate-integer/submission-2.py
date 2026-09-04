class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    #def duplicate():
    #nums = [1,2,3,3]
        '''
        i=0
        size = len(nums)
        while(i<size) :
            j=i+1
            while(j<size):
                if nums[i] ==nums[j] :
                    return True
                j=j+1
            i=i+1
        return False

        '''

        #nums= [1,2,3,3]
        size = len(nums)
        #print(nums,size)
        sett = set(nums)
        size2 = len(sett)
        #print(sett ,size2)
        if size > size2 :
            return True
        return False
#a = duplicate()
#print(a)
