class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # 1
        if sum(gas) < sum(cost):
            return -1
        
        # 2
        diff = [0] * len(gas)
        for i in range(len(gas)):
            diff[i] = gas[i] - cost[i]
        
        # 3
        total = 0
        result = 0

        # 4
        for i in range(len(diff)):
            total += diff[i]
            if total < 0:
                total = 0
                result = i + 1
        
        # 5
        return result 