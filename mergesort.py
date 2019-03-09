def merge_sort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        front = mylist[:mid]
        back = mylist[mid:]
        front = merge_sort(front)
        back = merge_sort(back)
        return merge(front, back)
    else:
        return mylist


def merge(front, back):
    """
    Merges the input arrays into a sorted
    array. Merge expects front and back to
    already be sorted.
    """
    i = 0
    j = 0
    k = 0
    returnlist = [None] * (len(front) + len(back))
    while i < len(front) and j < len(back):
        if front[i] < back[j]:
            returnlist[k] = front[i]
            i += 1
            k += 1
        else:
            returnlist[k] = back[j]
            j += 1
            k += 1

    # add the rest items to the merged list if one of the halfs is finished
    while i < len(front):
        returnlist[k] = front[i]
        i += 1
        k += 1

    while j < len(back):
        returnlist[k] = back[j]
        j += 1
        k += 1

    return returnlist


# if __name__ == "__main__":
    # merge_sort()
