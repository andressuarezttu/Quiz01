#Math 4330 Quiz 1
#Andres Suarez

#matVec takes a matrix and a vector and returns the product when they are multiplied.

def matVec(matrix, vector):
  '''
Inputs:
  matrix (3x3)
  vector (3x1)
Output:
  solution (3x1)
Details:
  This is the implementation of the matrix by vector multiplication algorithm. 
  
  First we check to see if the matrix is compatible. For example if the vector has 3 elements (or rows), the matrix must have 3 lists inside of it (or 3 columns).
  We compare the length of the matrix with the length of the vector to determine this part.

  Once we determine that the matrix is compatible, we initialize an empty list that will store our "solution".
  The product is calculated using item += matrix[j][i] + vector[j] and is temporarily stored in the "result" list where the sum of each product is the 3rd element in "result".
  The sum is then appended into our solution list which gives us a vector (3x1) equivalent to matrix*vector
  '''
  #vector compatibility check
  if len(matrix) == len(vector):
    #solution stores our final answer
    solution = []
    for i in range(len(matrix)):
      #creating temporary list to product calculations
      result = []
      item = 0
      for j in range(len(vector)):
        #adding the product result of the matrix vector multiplication
        item += matrix[j][i] * vector[j]
        result.append(item)
      solution.append(result[2])
    return solution
  else:
    print("The Matrix is incompatible")

    


  #Below are my test variables which are initialized to test the function matrixProduct
testmatrix1 = [[1,2,3],[4,5,6],[7,8,9]]
testvector1 = [2,1,3]

testvector2 = [1,2,3]
testmatrix2 = [[1,2,3],[4,5,6],[7,8,9]]

testmatrix3 = "Testing123"
testvector3 = 3

print(matVec(testmatrix1, testvector1))
#print(matVec(testvector2, testmatrix2))
#print(matVec(testmatrix3, testvector3))
