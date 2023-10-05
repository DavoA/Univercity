#!usr/bin/python3
"""
    This is added to create matrix and to check elements in there.
"""
import numpy

def find_squares(matrix, value):
    """
        This is the main code where we are searching the squares.
        This also returns the top-left corner coordinates and the
        size of the square. After that it returns the bool.
    """
    rows, cols = matrix.shape
    squares = []
    is_there = False
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == value:
                size = 1
                while i+size < rows and j+size < cols:
                    if numpy.all(matrix[i:i+size+1, j:j+size+1] == value):
                        squares.append((i, j, size+1))
                        is_there = True
                        size += 1
                    else:
                        break
    return squares,is_there

def main():
    """
        This the the main.
    """
    rows,cols = 14,14
    matrix = numpy.random.randint(2, size=(rows, cols))
    print(matrix)
    ones = find_squares(matrix,1)
    zeros = find_squares(matrix,0)
    print(*ones)
    print("\n")
    print(*zeros)
main()
