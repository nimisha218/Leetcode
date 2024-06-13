from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        # Define a recursive dfs method
        def dfs(node):

            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)

        # Build the graph
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        # Initialize a seen set
        seen = set()

        ans = 0

        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        
        return ans

        

                 


