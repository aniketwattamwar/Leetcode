class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        # got the logic and implemented as well
        # struggled with the adjacent pairs before and after check
        colors = [0 for i in range(n)]
        print(colors)
        result = []
        count =0
        for idx, color in queries:
            if colors[idx] != 0:
                if idx > 0 and colors[idx] == colors[idx - 1]:
                    count -= 1
                if idx < n - 1 and colors[idx] == colors[idx + 1]:
                    count -= 1

            colors[idx] = color
            if idx > 0 and colors[idx] == colors[idx - 1]:
                count += 1

            if idx < n - 1 and colors[idx] == colors[idx + 1]:
                count += 1

            result.append(count)

        print(colors)

        return result



        