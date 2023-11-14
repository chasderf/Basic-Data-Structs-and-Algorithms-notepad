from collections import deque

data = deque()
data.append("Charlie")
element = data.popleft()

print(element, data)