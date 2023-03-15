
### IMPORTS

import numpy as np

## FUNCTION FOR SET UNION
def set_union(set1, set2):

    array = set1

## THIS ITERATES OVER THE SECOND SET AND ADDS ANY VALUES THAT ARE NOT IN THE FIRST ONE
    for i in set2:
        if np.isin(i, array):
            continue

        array = np.append(array, i)

    return array


## FUNCTION FOR SET INTERSECTION
def set_intersection(set1, set2):

    array = np.array([])

## ITERATES THROUGH FIRST SET AND APPENDS ANY VALUE THAT ISNT IN THE SECOND SET TO THE "DIFFERENCE" LIST
    for i in set1:
        if np.any(i == set2):
            array = np.append(array, i)

    return array



## FUNCTION FOR SET DIFFERENCE
def set_difference(set1, set2):

## PUTS SETS AS LISTS TO SAVE ORDER
    list1 = set1.tolist()
    list2 = set2.tolist()

    difference = []

## ITERATES THROUGH FIRST SET AND APPENDS ANY VALUE THAT ISNT IN THE SECOND SET TO THE "DIFFERENCE" LIST
    for i in list1:
        if i not in list2:
            difference.append(i)

    array = np.array(difference)
## RETURNS NUMPY ARRAY
    return array




## DEFINING SetCalculator function
def SetCalculator(file1, file2):

### LOADING SETS AS NUMPY ARRAYS FOR EASIER COMPUTATION
    sets1 = np.loadtxt(fname=file1, dtype=str)


### SAVING SETS IN A DICTIONARY
    dictionary = {}

    for i in range(len(sets1)):
        dictionary[sets1[i][0]] = sets1[i][1:]


#### LOADING OPERATIONS
### I used the python file reading functions instead of the numpy because the numpy functions have issues
### with rows that have a varying number of columns, so this allows for files that have operations of different lengths
    ops = open(file2, 'r')
    ops1 = ops.readlines()


    for i in range(len(ops1)):

        ops1[i] = ops1[i].split()
# REMOVES WHITESPACE


        num_operations = (len(ops1[i]) - 1)/2
# CALCULATES NUMBER OF SET OPERATIONS ON LINE


        new_set = dictionary[ops1[i][0]]
        ops1[i][0] = new_set
# SETS THE FIRST VARIABLE OF LINE TO ITS CORRESPONDING SET


        while num_operations > 0 and len(ops1) != 1:
#ENSURES THE CORRECT NUMBER OF SET OPERATIONS ARE COMPUTED

#UNION OPERATION
            if ops1[i][1] == 'U':
                new_set = set_union(new_set,dictionary[ops1[i][2]])

                ops1[i][0] = new_set
                ops1[i].pop(1)
                ops1[i].pop(1)
#REPLACES THE ORIGINAL SET WITH THE UNIONIZED SET AND REMOVES THE SET OPERATION AND SECOND VARIABLE FROM THE LINE


                num_operations = int(num_operations - 1)
#REDUCES NUMBER OF OPERATIONS BY 1


#INTERSECTION OPERATION
            elif ops1[i][1] == 'I':
                new_set = set_intersection(new_set, dictionary[ops1[i][2]])

                ops1[i][0] = new_set
                ops1[i].pop(1)
                ops1[i].pop(1)
# REPLACES THE ORIGINAL SET WITH THE INTERSECTED SET AND REMOVES THE SET OPERATION AND SECOND VARIABLE FROM THE LINE

                num_operations = int(num_operations - 1)

            elif ops1[i][1] == '-':
                new_set = set_difference(new_set, dictionary[ops1[i][2]])

                ops1[i][0] = new_set
                ops1[i].pop(1)
                ops1[i].pop(1)
# REPLACES THE ORIGINAL SET WITH THE DIFFERENTIATED SET AND REMOVES THE SET OPERATION AND SECOND VARIABLE FROM THE LINE

                num_operations = int(num_operations - 1)



    flat_ops1 = [array[0] for array in ops1]
    ## UNPACKS OPS1 FROM EXTRA LIST

    for i in range(len(flat_ops1)):
        if len(flat_ops1[i]) < 1:
            flat_ops1[i] = "Empty Set"
    ##Replaces empty numpy arrays


    with open("output.txt", "w") as f:
        for i in flat_ops1:
            np.savetxt(f, [i], delimiter=" ", fmt="%s")


    ### WRITES FLAT_OPS1 TO OUTPUT FILE "output.txt"



if __name__ == "__main__":

    print('Please make sure files are in current working directory and give file names')

    SetCalculator(file1 = input("Set File: "), file2 = input("Operation File: "))




