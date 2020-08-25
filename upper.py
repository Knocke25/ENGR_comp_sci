def Upper(Aaug):
    s = [0]*len(Aaug)
    a = [0]*len(Aaug)
    for col in range(len(Aaug)-1, 0, -1):
        for row in range(0, col, 1): #start stop step
            x = Aaug[row][col]
            y = Aaug[row+1][col]
            for i in range(len(Aaug)+1):
                Aaug[row][i] = ((Aaug[row][i])*y)-((Aaug[row+1][i])*x)
    for j in range(0, len(Aaug), 1):
        for k in range(len(Aaug)):
            if j != k:
                s[j] = s[j]-Aaug[j][k]*a[k]
        a[j] =((Aaug[j][len(Aaug)])+(s[j]))/(Aaug[j][j])
    return a

def main():
    Matrix = ([2, 7, 3, 6, 2],
              [3, 3, 4, 4, 6],
              [6, 9, 5, 3, 3],
              [4, 2, 1, 7, 5])
    print('The x value solutions to the Gauss elimination are: ', Upper(Matrix))
main()