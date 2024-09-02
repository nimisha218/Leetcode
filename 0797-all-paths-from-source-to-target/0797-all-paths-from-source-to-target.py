class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def backtrack(curr, node):

            if node == n - 1:
                result.append(curr[:])
                return
            
            for label in graph[node]:
                curr.append(label)
                backtrack(curr, label)
                curr.pop()
        
        n = len(graph)
        result = []
        backtrack([0], 0)
        return result


