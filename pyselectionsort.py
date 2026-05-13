def selection(mat):

    for i in range(len(mat)):

        min = i
        for j in range(1+i,len(mat)):

            if mat[j]<mat[min]:
                min = j

        mat[i],mat[min] = mat[min], mat[i]

    return mat


mat = [12,12,34,55,4,3,2,4,1,56,65,4]
print(selection(mat))