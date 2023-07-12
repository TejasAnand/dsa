class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum=nums[0]

        #implementing binary search here 

        lo = 0
        hi = len(nums)-1

        while lo<=hi:
            mid = (lo+hi)//2

            if nums[lo]<nums[hi]:
                minimum= min(nums[lo],minimum)
                break
            minimum = min(minimum,nums[mid])
            if nums[mid]>=nums[lo]:
                lo = mid+1  #searching right
            else:
                hi = mid-1  #searching left
        return minimum