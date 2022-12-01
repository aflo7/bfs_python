class Node:
    def __init__(self, name, pi, distance, color):
        self.name = name
        self.pi = pi
        self.distance = distance
        self.color = color

    def __str__(self):
        return self.name