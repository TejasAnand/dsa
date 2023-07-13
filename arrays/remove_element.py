class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        #initializing left_pointer

        left_ptr=0

        #initializing right_pointer(with iteration)
        for right_ptr in range(0,len(nums)):
            if nums[right_ptr]!= val:
                nums[left_ptr]=nums[right_ptr]
                left_ptr+=1
        return left_ptr
