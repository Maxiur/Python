import random

class BinaryCounter:
    def __init__(self):
        self.state = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.state ^= 1
        return self.state

n = 20

# Test:
counter = BinaryCounter()
for _ in range(n):
    print(next(counter), end=" ")

print()

class RandomDirection:
    def __init__(self):
        self.directions = ["N", "E", "S", "W"]

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.directions)

pedestrian = RandomDirection()
for _ in range(n):
    print(next(pedestrian), end=" ")

print()

class WeekIterator:
    def __init__(self, start_day=0):
        self.current = start_day % 7

    def __iter__(self):
        return self

    def __next__(self):
        # zeby nie było -1 jesli start=0
        val = self.current
        self.current = (self.current + 1) % 7
        return val

days = WeekIterator(2)
for _ in range(n):
    print(next(days), end=" ")