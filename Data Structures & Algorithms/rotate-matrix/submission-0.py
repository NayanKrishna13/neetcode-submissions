class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i=0
        for length in range(len(matrix),-1,-2):
            #print(length)
            for j in range(i,i+length-1):
                k=i+length-1
                matrix[j][i],matrix[i][k-(j-i)],matrix[k-(j-i)][k],matrix[k][j]=matrix[k][j],matrix[j][i],matrix[i][k-(j-i)],matrix[k-(j-i)][k]
                #print(matrix)
            i+=1 

            