#!usr/bin/python3
"""
    Սա ստեղծված է մատրիցա ստեղծելու և այնտեղ տարրերը ստուգելու համար:
"""
import numpy
def find_squares(matrix, value):
    """
        Սա այն հիմնական կոդն է, որտեղ մենք փնտրում ենք քառակուսիները:
        Սա նաև վերադարձնում է քառակուսու վերևի ձախ անկյունի կոորդինատները և
        այդ քառակուսու չափը. Դրանից հետո այն վերադարձնում է բուլյան արժեքը:
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
        Սա մեր հիմնական ֆունկցիան է որի մեջ մենք կանչում ենք բոլոր 
        մեր գրած ֆունկցիաները:
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
