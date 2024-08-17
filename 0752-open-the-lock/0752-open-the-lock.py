from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def getNeighbors(node):

            neighbors = []
            for i in range(4):
                num = int(node[i])
                for change in [-1, 1]:
                    x = (num + change) % 10
                    neighbors.append(node[:i] + str(x) + node[i+1:])
            return neighbors

        
        seen = set(deadends)
        seen.add(("0000"))

        queue = deque([("0000", 0)])

        if "0000" in deadends or target in deadends:
            return -1
        
        while queue:

            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                node, steps = queue.popleft()
                if node == target:
                    return steps
                for neighbor in getNeighbors(node):
                    if neighbor not in seen:
                        queue.append((neighbor, steps + 1))
                        seen.add((neighbor))
        
        return -1


