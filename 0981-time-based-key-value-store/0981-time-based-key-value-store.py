from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[value, timestamp]]
        else:
            self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        result = ""

        if key in self.store:

            values = self.store[key]

            left = 0
            right = len(values) - 1

            while left <= right:

                mid = (left + right) // 2

                if values[mid][1] <= timestamp:
                    result = values[mid][0]
                    left = mid + 1
                
                else:
                    right = mid - 1
        
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)