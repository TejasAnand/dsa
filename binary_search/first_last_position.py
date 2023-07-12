class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.binary_search(nums,target,True)
        right = self.binary_search(nums,target,False)

        return [left,right]

        #implementing binary search first

    
    def binary_search(self,nums,target,left_repeating):
        lo=0
        hi = len(nums)-1
        i=-1
        while lo<=hi:

            mid = (lo+hi)//2

            if nums[mid]>target:
                hi = mid-1

            elif nums[mid]<target:
                lo=mid+1

            else:
                i=mid
                if left_repeating:
                    hi = mid-1
                else:
                    lo=mid+1
            
        return i



        