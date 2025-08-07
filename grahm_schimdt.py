import numpy as np

def orthogonalisation(a):
    (n,m) = a.shape
    
    for i in range(m):
        #i-th column of a
        q = a[:,i]

        for j in range(i):
            q = np.dot(a[:,j],a[:,i]) *a[:,j]
        
        if np.array_equal(q, np.zeros(q.shape)):
            raise np.linalg.LinAlgError("the  column vectors are not linearly independent")

        #noramlize q
        q = q/np.sqrt(np.dot(q,q))

        a[:,i] = q

#driver code

vect = np.array([
    [3.0,2.0,1.0],
    [-2.0,0.5,2.5],
    [1.0,1.0,-3.0]
])

orthogonalisation(vect)

print(vect)
