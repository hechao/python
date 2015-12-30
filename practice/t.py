def median(list):
    if len(list) %2 == 0:
        k = list[len(list)/2]
    elif len(list) == 1:
        k = list[0]
    else:
        list = list.sorted(list)
        k = (float(list[len(list)/2])+float(list[len(list)/2+1]))/2
    return k

median([4, 5, 5, 4])
