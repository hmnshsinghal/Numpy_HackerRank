#################### ARRAY INDEXING #################################

import numpy as np

def array_index(n,n_row,n_col):
    l1=np.arange(n).reshape(n_row,n_col)
    print(l1[-1])
    mid_lt=[]
    for i in range(len(l1)):
        ln=len(l1[0])
        if ln%2!=0:
            ln=int((ln-1)/2)
            mid_lt.append(l1[i][ln])
        else :
            ln=int((ln-2)/2)
            mid_lt.append(l1[i][ln])
    print(np.array(mid_lt))
    print(np.array([list(l1[0][-3:]),list(l1[1][-3:])]))


##########################################ARRAY CREATION#######################################
def array_operations(l):
    #Write your code below
    npr=np.array(l)
    print(type(npr))
    print(npr.ndim)
    print(npr.shape)
    print(npr.size)
 

#######################Determine Attributes ######################
def array_attributes(l):
    #write your code here
    npr=np.array(l)
    print(type(npr))
    print(npr.ndim)
    print(npr.shape)
    print(npr.size)
    print(npr.dtype)
    print(npr.itemsize)
 ###################NDARRAY####################
 def ndarray(array_input):
    #Write your code here
    npr=np.array(array_input)
    print(npr.ndim)
    print(npr.shape)
    print(npr.size)
    
 #################ndarray and Shape###########
def ndshape(d, shape1):
    #Write your code here
    dm=[]
    #print(np.arange(d))#.shape(shape1))
    for i in range(0,d):
        for j in range(0,d):
            if i == j:
               dm.append(1.)
            else :
                dm.append(0.)
    print(np.reshape(np.array(dm),(d,d)))
    j=1
    for i in shape1:
        j=j*i
    l2=[]
    for i in range(j):
        l2.append(1.)
    #print(l2)
    print(np.reshape(np.array(l2),(shape1)))
    
##############ndarray#############
    #Write your code here
    l1=[]
    for i in range(1,a):
        if i%2==0:
            l1.append(i)
    print(np.array(l1))
    print(np.linspace(x,y, num = z))
    
##########ARRAY 1##############
def array_oper(num1,num2):
    x=np.reshape(np.arange(num1,num2+1),(2,3))
    for i in range(len(x)):
        for j in range(len(x[i])):
            k=x[i][j]
            x[i][j]=k**2+5
    print(x)
    
#############ARRAY 2############
def array_oper(num1,num2):
    l1=[]
    np.random.seed(100)
    for i in range(30):
        l1.append(np.random.randint(num1,num2))
    
    l2=np.reshape(l1,(5,6))
    #print(l2)
    print(np.sum(l2,axis=0)[-1])
    print(np.sum(l2,axis=1)[-1])
    
############### Normalization ################
import ast
import numpy as np

# Enter your code here. Read input from STDIN. Print output to STDOUT
def array_oper(n,m,sd):
    np.random.seed(100)
    s = np.random.normal(m, s, n)
    print(np.mean(s))
    print(np.std(s))
    print(np.var(s)) 
 
 ##################ARRAY MANIPULATION 1####################
 import numpy as np

# Enter your code here. Read input from STDIN. Print output to STDOUT
def array_split(i,r,c):
    #Write your code below
    #print(i,r,c)
    x=np.arange(i)
    y=np.reshape(x,(r,c))
    na=np.hsplit(y,2)
    print(na[0])
    print(na[1])

    
##########################ARRAY MANIPULATION 2################
import ast
import numpy as np

# Enter your code here. Read input from STDIN. Print output to STDOUT
def array_split(n,n_row,n_col):
    x=np.arange(n)
    z=np.reshape(x,(n_row,n_col))
    vr=np.vsplit(z,2)
    print(vr[0])
    print(vr[1])    

#############JOIN ARRAYS##############
def join_array(list1,list2):
    l1=np.reshape(list1,(2,2))
    l2=np.reshape(list2,(2,3))
    #print(l1,l2)
    print(np.concatenate((l1, l2), axis=1))
    
 ##################Slicing#################
 def array_slice(n,n_dim,n_row,n_col):
    #print(n,n_dim,n_row,n_col)
    x=np.arange(n)
    y=np.reshape(x,(n_dim,n_row,n_col))
    b = np.array([True, False], dtype=bool)
    #print(b)
    print(y[b])
    print(y[b,:,1:3])
    
############ 3D Array #############
def array_3d(n, x, y, z):
    #Write your code below
    np.random.seed(100)
    x1=np.random.normal(5,2.5,n)
    print(x1.nbytes)
    print(np.random.rand(x,y,z))
