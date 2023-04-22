def multiply(A,B):
    try:
        multiplied = []
        for n in len(A):
            for m in len(B[0]):
                for u in len(A[n]):
                    multiplied.append(A[n][u]*B[u][n])
        return multiplied

    except:
        if len(A[0])!=len(B):  # Compatibility check
            raise Exception('Dimension mismatch')
        return Exception
        

A = [[1,2,3,4,5]]
B = [[10],
     [20],
     [30],
     [40],     
     [50]]

print(multiply(A,B))
