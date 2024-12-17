# Q3
# Triangular Number Sequence is generated from a pattern of dots that form a triangle
# The first 5 numbers of the sequence are
# 1, 3, 6, 10, 15

# Example:
# TriangularNumberSequence(3) => 6
# TriangularNumberSequence(6) => 21

def triangular (n):

    return n * (n + 1) // 2

n = int(input("Enter a number: "))

print(triangular(n))
