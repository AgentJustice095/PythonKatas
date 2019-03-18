import math
def chop(searchvalue, arraysearched, start = -1, stop = -1):
    arraystart = start
    arraystop = stop
    if arraystart == -1:
        arraystart = 0
    if arraystop == -1:
        arraystop = len(arraysearched)-1
    arraysize2 = int((arraystart + arraystop) / 2)


    if arraystart >= arraystop and arraysearched[arraysize2] == searchvalue:
        return arraysize2
    elif arraystart >= arraystop:
        return(-1)

    #Have we found our number
    if arraysearched[arraysize2] == searchvalue:
        return(arraysize2)
    elif arraysearched[arraysize2] > searchvalue:
        return(chop(searchvalue, arraysearched, start, arraysize2 - 1))
    else:
        return(chop(searchvalue, arraysearched, arraysize2 + 1, stop))

