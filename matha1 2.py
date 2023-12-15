f=open("math.txt","r")
fread=f.readlines()
fread2=[]                                 #creating a new list to strip "\n" from all lines
for i in fread:
    fread2+=[i.strip("\n")]                #fread2 is the list containing all entries of the file without "\n"
start=0
matrices=[]
for j in range(len(fread2)):               #making nested lists of all separate entries
    if fread2[j]=="":
        lst=fread2[start:j]
        start=j+1
        matrices+=[lst]
mxs=[]
for entry in matrices:                     #making a separate list mxs which contains all matrices in nested list form
    matrix=entry[2:]                           
    temp=[]
    for e in matrix:
        lst=list(map(int,e.split()))          
        temp+=[lst]
    mxs+=[temp]
print(mxs)
def rref(matrix):                          #defining a function for finding the RREF of a matrix
    pivot = 0
    row = len(matrix)
    col = len(matrix[0])
    for rows in range(row):
        if pivot >= col:
            return matrix
        i = rows
        while matrix[i][pivot] == 0:
            i += 1
            if i == row:
                i = rows
                pivot += 1
                if col == pivot:
                    return matrix
        matrix[i], matrix[rows] = matrix[rows], matrix[i]
        scaling_factor = matrix[rows][pivot]
        matrix[rows] = [ent / float(scaling_factor) for ent in matrix[rows]]
        for i in range(row):
            if i != rows:
                scaling_factor = matrix[i][pivot]
                matrix_temp=[]
                for k in range(col):
                    initial=matrix[i][k]
                    other=matrix[rows][k]
                    matrix_temp+=[initial-scaling_factor*other]
                matrix[i]=matrix_temp
        pivot += 1
    return matrix                     
for entry in mxs:                              
    row=len(entry)
    rref_matrix=rref(entry)                         #calling the rref function
    pivots=[]
    for rows in range(row):
        for entries in entry[rows]:
            if entries==1:
                ind=entry[rows].index(entries)
                tup=(rows,ind)
                pivots+=[tup]                         #creating a tuple containg all pivot positions
    print("\nPIVOT POSITIONS:")
    print(pivots,"\n")
    print("RREF:")
    for j in rref_matrix:                              #printing the RREF matrix
        print(j)
    print("\nSOLUTION:")
    zero=[0 for i in range(len(entry[1]))]            #making a zero list for the trivial solution      
    print(zero,end=" ")
    pivot_columns=[pivot[1] for pivot in pivots]
    non_pivot_columns=[cols for cols in range(len(entry[1])) if cols not in pivot_columns]
    for free in non_pivot_columns:
        lst=[]
        row=0
        for i in range(len(entry[1])):
            if i in pivot_columns:
                if rref_matrix[row][free]==0.0:
                    lst+=[0.0]
                else:
                    lst+=[-(rref_matrix[row][free])]
                row+=1
            if i == free:
                lst+=[1]
            elif i in non_pivot_columns:
                lst+=[0]
        print("+","x_"+str(free)+"*",lst,end="")
    print("-"*30)
        
    
    



        
        
    


        





