import scipy.io 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

mat = scipy.io.loadmat('POS.mat')

# the file POS contains a graph that shows the amount of interaction between
# Vdifferent proteins (nodes). If there is no interaction, then there is
# no connection. The graph is give below:

A=mat['network']
m,_=A.shape

# The graph in A is in the compressed sparse row format. The edges are also
# weighted (A.value), but we do not use these valuse. We can split A
# to train and test and also change it to a coordinated representation,
# which is easier to work with:

R, T = train_test_split(A, test_size=0.2)
pos_train=R.tocoo()
pos_test=T.tocoo()

# Now, we create the negative set which has two rows for the indices of the two
# nodes of an edge i.e. (u,v)

neg_size=alpha*A.nnz
neg_set=np.random.randint(0,m,(2,neg_size))


# Here is the code for count the number of false positives/ negatives

def pred_test(U):
    FN=0
    for ind in range(pos_test.nnz):
        a=pos_test.row[ind]
        b=pos_test.col[ind]
        nodds=np.inner(U[:,a],U[:,b])
        if (nodds<0):
            FN+=1
    FP=0
    for ind in range(neg_size):
        a=neg_set[0, ind]
        b=neg_set[1, ind]
        nodds=np.inner(U[:,a],U[:,b])
        if (nodds>0):
            FP+=1        
    return FN/pos_test.nnz, FP/neg_size


# Main code goes here

iter_num=int(5e5)
step=.1

# Initialize U

d=5
U=.1*np.random.randn(d,m)/np.sqrt(d)



# Write your SGD code here note that since you run many iterations, call
# the function pred_test at the end of each epoch
# You can also write a function to track the vaue f the objective function

for iter in range(iter_num):
    ...

