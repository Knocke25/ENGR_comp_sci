

def GaussElim(Aaug):
    N=len(Aaug) # the number of equations

    # the elimination
    for pivot in range(N-1):  # don't use the last row as a pivot
        pivotTerm = Aaug[pivot][pivot] # we sure hope it isn't ZERO
        if pivotTerm == 0:                                                          # check if zero
            Aaug[pivot], Aaug[pivot+1] = Aaug[pivot+1], Aaug[pivot]                 # switch row and next row
            pivotTerm = Aaug[pivot][pivot]                                          # set new pivot term
        for row in range(pivot+1,N): # loop to the last row
            R=Aaug[row][pivot]/pivotTerm
            Aaug[row][pivot] = 0
            for col in range(pivot+1,N+1):  # loop to the last col
                Aaug[row][col] -= Aaug[pivot][col]*R
            # next col
        #next row
    #next pivot

    # back substitution   ...  subscripts are TRICKY
    x=[0]*N # create a place to store the solution
    for row in range(N-1,-1,-1): # all rows ... backwards
        x[row]= Aaug[row][N]  # the RHS value for this row
        for col in range(row+1,N):  # to the end of the unaugmented A matrix
            x[row] -= Aaug[row][col]*x[col]  # subtracting the appropriate value
        # next col
        x[row] = x[row]/Aaug[row][row]  # and divide by the diagonal term
    #next row

    return x

def main():
    Aaug=[[1, 2, 5, 3, 2],
          [0, 0, 4, 1, 6],
          [0, 3, 1, 5, 2],
          [0, 4, 3, 5, 2]]
    print(GaussElim(Aaug))

main()