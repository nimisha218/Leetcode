class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        directions = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}

        visited = set()
        current = tuple((0, 0))
        visited.add(current)

        for p in path:

            dx, dy = directions[p]
            current = tuple((current[0] + dx, current[1] + dy))
            if current in visited:
                return True
            visited.add(current)

        return False
