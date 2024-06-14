from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        # Define a recursive dfs method
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node, neighbor) in roads:
                        ans[0] += 1
                    seen.add(neighbor)
                    dfs(neighbor)

        # Build the graph
        graph = defaultdict(list)
        roads = set()
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
            roads.add((i, j))
        
   
        # Compute the solution
        seen = {0}
        ans = [0]
        dfs(0)
        return ans[0]



        
                
        

        




