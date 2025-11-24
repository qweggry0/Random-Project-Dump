# Pascals triangle
# Iterative Approach

def PascalTriangle(n):
    triangle = [[1, 1]]
    subset = []
    for j in range(n-1):
        subset = []
        for i in range(len(triangle[j])-1):
            subset.append(triangle[j][i] + triangle[j][i+1])
        subset.insert(0, 1)
        subset.insert(len(triangle[j]), 1)
        triangle.append(subset)

    return triangle





def DisplayTriangle(triangle, n=-1):
    if n == -1: 
        for i in triangle:
            print(i)
    else:
        for i in range(n):
            print(triangle[i])


        


DisplayTriangle(PascalTriangle(1000))

