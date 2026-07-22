import numpy as np

def rref(matrix):
    matrix=matrix.astype(np.float64)
    curr_p=0
    for lead in range(len(matrix[-1])):
        for pivot in range(curr_p,len(matrix)):
            if matrix[pivot][lead]==0:
                new_pivot=np.argmax(np.abs(matrix[pivot:,lead]))+pivot
                matrix[[pivot,new_pivot]]=matrix[[new_pivot,pivot]]
            if matrix[pivot][lead]!=0:
                matrix[pivot]=matrix[pivot]/matrix[pivot][lead]
                for other in range(len(matrix)):
                    if other!=pivot:
                        matrix[other]-=matrix[pivot]*(matrix[other][lead]/matrix[pivot][lead])
                curr_p+=1
                break
    return matrix


