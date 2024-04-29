class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def backtrack(curr, next):

            if next == len(graph) - 1:
                ans.append(curr[:])
                return

            if next not in curr:
                curr.append(next)

            for node in graph[next]:
                curr.append(node)
                backtrack(curr, node)
                curr.pop()
        
        ans = []
        backtrack([], 0)
        return ans