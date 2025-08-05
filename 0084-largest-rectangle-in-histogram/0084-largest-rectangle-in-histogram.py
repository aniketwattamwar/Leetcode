class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # did not fully understand tbh
        # revisit this
        stack = []
        max_area = 0
        heights.append(0)
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]] > h: 
                popped = stack.pop()
                ht_popped = heights[popped]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                max_area = max(max_area, width*ht_popped)

            stack.append(i)

        return max_area

            
        