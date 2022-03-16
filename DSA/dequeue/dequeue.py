import collections

DoubleEnded = collections.deque(["Mon", "Tue", "Web"])
print(DoubleEnded)

DoubleEnded.append("Thu")

print("Append at right - ")
print(DoubleEnded)

DoubleEnded.appendleft("Sun")
print("Append at left is - ")
print(DoubleEnded)

DoubleEnded.pop()
print("Deleting from right - ")
print(DoubleEnded)

DoubleEnded.popleft()
print("Deleting from left -")
print(DoubleEnded)