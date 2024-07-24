from collections import defaultdict

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        outgoing = defaultdict(int)
        cities = set()

        for path in paths:
            outgoing[path[0]] = 1
            cities.add(path[0])
            cities.add(path[1])
        
        for city in cities:
            if city not in outgoing:
                return city
        

        