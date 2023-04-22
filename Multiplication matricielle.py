# Schiltz Thomas - April 2023
def multiply(A,B):
    if len(A[0])!=len(B):  # compatibility check
        raise Exception('Dimension mismatch')
    multiplied = [] # end matrix
    for n in range(0,len(A)):
        """

        a-> A | B  b-> E | F
            C | D      G | H

        a = [[A,B],[C,D]]
        b = [[E,F],[G,G]]
        
            we begin with iterating on the number of columns in A

        """
        row = [] 
        for u in range(0,len(B[0])): # here we iterate on the length of one row of B
            added = 0 # total of sums 
            for m in range(0,(len(B))): # iterating on the number of columns in B
                added = added + A[n][m]*B[m][u]
            row.append(added)  # we add the answer to the current row 
        multiplied.append(row) # once the row is done, we add it to the matrix
    return multiplied
