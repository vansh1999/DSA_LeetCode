class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort

        # def get_start(interval):
        #     return interval[0]
        # intervals.sort(key=get_start)

        intervals.sort(key = lambda interval: interval[0])

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0] , max(merged[-1][1] , interval[1])]
        return merged

sol = Solution()
print(sol.merge([[4,7],[1,4]]))

# time complexity -> O(n log n) + n => O(llogn)
# sort() -> nlogn
# for -> n
# = n log n + n 

# Space -> O(n)
