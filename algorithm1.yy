import math

# Function to calculate the Euclidean distance between two points
def distance(p1, p2):
    # Calculate the Euclidean distance between two points
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Naive brute force algorithm to find the closest pair of points
def closest_pair_naive(points):
    # Edge case: if there are fewer than two points, return None
    if len(points) < 2:
        return None, float('inf')

    min_dist = float('inf')
    pair = None  # To store the closest pair of points

    # Compare every point with every other point
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])  # Calculate distance between points
            if dist < min_dist:  # If this distance is smaller, update the closest pair
                min_dist = dist
                pair = (points[i], points[j])
    
    # Return the closest pair and their distance
    return pair, min_dist

# Example usage
points = [(1, 2), (3, 4), (6, 1), (7, 8)]
pair, dist = closest_pair_naive(points)
print("Closest Pair:", pair)
print("Distance:", dist)





