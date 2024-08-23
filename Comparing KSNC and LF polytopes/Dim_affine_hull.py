import numpy as np

# Example of format of input .txt valid file_path

#[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
#[1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
#...

def read_points_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    points = []
    for line in lines:
        # Parse the string representation of the list into a Python list of floats
        point = list(map(float, line.strip()[1:-1].split(', ')))
        points.append(point)
    
    return np.array(points)

def affine_hull_dimension(points):
    # Choose the first point as the reference point
    reference_point = points[0]
    
    # Create a matrix of difference vectors
    diff_vectors = points[1:] - reference_point
    
    # The rank of this matrix is the dimensionality of the affine hull
    rank = np.linalg.matrix_rank(diff_vectors)
    
    return rank

file_path = 'Pa_respects_Ineq15.txt'  # Replace with any file_path of interest
points = read_points_from_file(file_path)
print(points)
dimension = affine_hull_dimension(points)
print(f"The dimensionality of the affine hull is: {dimension}")
