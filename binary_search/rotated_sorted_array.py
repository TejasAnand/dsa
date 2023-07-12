class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lo = 0
        hi = len(nums)-1

        while lo<=hi:
            mid = (lo+hi)//2

            if nums[mid]==target:
                return mid
            
            elif nums[mid]>=nums[lo]:
                if nums[lo]<=target<=nums[mid]:
                    #search left
                    hi=mid-1
                else:
                    lo=mid+1
            else:
                if nums[mid]<=target<=nums[hi]:
                    #search right
                    lo=mid+1
                else:
                    hi=mid-1
                    
        return -1