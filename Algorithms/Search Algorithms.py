def linear_search(values, search_for):
    search_at = 0
    search_res = False
    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at = search_at + 1

    return search_res


def interpolation_search(values, x):
    index0 = 0
    index_n = (len(values) - 1)
    while index0 <= index_n and values[index0] <= x <= values[index_n]:
        mid = index0 + int(((float(index_n - index0) / (values[index_n] - values[index0])) * (x - values[index0])))
        if values[mid] == x:
            return "Found " + str(x) + " at index " + str(mid)
        if values[mid] < x:
            index0 = mid + 1
    return "Given element is absent from the list"
