class Solution:
    def maxArea(self, height: List[int]) -> int:

        # length is basically the width here

        # amount of water is basically length*width

        # length here is min(height[left_ptr],[right_ptr])

        # width is always right_ptr-left_ptr

        # initialising pointers

        left_ptr = 0
        water = 0

        right_ptr = len(height)-1

        while left_ptr < right_ptr:
            # amount of water is:
            area = min(height[left_ptr], height[right_ptr]) * \
                (right_ptr-left_ptr)
            water = max(area, water)
            if height[left_ptr] <= height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        return water
