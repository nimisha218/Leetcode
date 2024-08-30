from collections import defaultdict
from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        red = defaultdict(list)
        blue = defaultdict(list)

        for edge in redEdges:
            red[edge[0]].append(edge[1])
        for edge in blueEdges:
            blue[edge[0]].append(edge[1])
        
        answer = [-1 for i in range(n)]

        queue = deque([[0, 0, None]]) # [node, length, prev_edge_color]

        visited = {(0, None)} # (node, prev_edge_color)

        while queue:

            num_nodes = len(queue)

            for _ in range(num_nodes):

                node, length, edge_color = queue.popleft()

                if answer[node] == -1:
                    answer[node] = length
                
                if edge_color != "RED":
                    for neighbor in red[node]:
                        if (neighbor, "RED") not in visited:
                            visited.add((neighbor, "RED"))
                            queue.append([neighbor, length + 1, "RED"])
                
                if edge_color != "BLUE":
                    for neighbor in blue[node]:
                        if (neighbor, "BLUE") not in visited:
                            visited.add((neighbor, "BLUE"))
                            queue.append([neighbor, length + 1, "BLUE"])
        
        return answer
