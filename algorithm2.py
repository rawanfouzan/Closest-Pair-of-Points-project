import math
from sortedcontainers import SortedSet

# Point class for 2-D points
class Point:
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    # Define equality: two points are equal if their coordinates are equal
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    # Define hash: makes the object hashable (required for set/dict operations)
    def __hash__(self):
        return hash((self.x, self.y))

    # Less Than (Required for ordering in irange when using key function)
    def __lt__(self, other):
        # Compare based on the set's key: (y, x)
        if self.y != other.y:
            return self.y < other.y
        return self.x < other.x


def closestPair(coordinates, n) :



	# Sort points according to x-coordinates
    coordinates.sort(key=lambda p: p.x)

    # SortedSet to store already processed points whose distance from the current points is less than the smaller distance so far
    s = SortedSet(key=lambda p: (p.y, p.x))

    squaredDistance = 1e18
    best_pair = None
    j = 0

    for i in range(len(coordinates)):
        # Find the value of D
        D = math.ceil(math.sqrt(squaredDistance))
        while j < i and coordinates[i].x - coordinates[j].x >= D:
            s.discard(coordinates[j])
            j += 1

        # Find the first and last point in the set whose y-coordinate is less than D distance from ith point
        start = Point(coordinates[i].x, coordinates[i].y - D)
        end = Point(coordinates[i].x, coordinates[i].y + D)

        # Iterate over all such points and update the minimum distance
        for it in s.irange(start, end):
            dx = coordinates[i].x - it.x
            dy = coordinates[i].y - it.y
            dist2 = dx * dx + dy * dy
            if dist2 < squaredDistance:
                best_pair = (coordinates[i], it)
            squaredDistance = min(squaredDistance, dist2)

        # Insert the point into the SortedSet
        s.add(coordinates[i])

    return math.sqrt(squaredDistance), best_pair


# Driver code
if __name__ == "__main__":
    # Points on a plane P[i] = {x, y}
    P = [
        Point(1, 2),
        Point(6, 3),
        Point(5, 1),
        Point(1, 2.5),
        Point(7, 9)
    ]
	
    
    # Function call
    distance, pair = closestPair(P, len(P))
    print("Smallest distance:", distance)
    print("Closest pair: ({}, {}) and ({}, {})"
          .format(pair[0].x, pair[0].y, pair[1].x, pair[1].y))

    

