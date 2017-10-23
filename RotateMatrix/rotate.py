	for i in range(len(matrix)/2):
            for j in range (len(matrix) - i*2 -1):
                temp = matrix[i][i+j]
                
                matrix[i][i+j] = matrix[len(matrix)-1-i-j][i]
                matrix[len(matrix)-1-i-j][i] = matrix[len(matrix)-1-i][len(matrix)-1-i-j]
                matrix[len(matrix)-1-i][len(matrix)-1-i-j] = matrix[i+j][len(matrix)-1-i]
                matrix[i+j][len(matrix)-1-i]= temp