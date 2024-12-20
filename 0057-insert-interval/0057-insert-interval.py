class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []

        for i in range(len(intervals)):

            # If the newInterval appears before the current interval 
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            
            # If the newInterval appears after the current interval
            if newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            
            # There is an overlap
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        result.append(newInterval)

        return result

            
           


        

