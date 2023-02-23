def binary_search(data, key):
    l = 0
    h = len(data)

    while l<=h:
        m = int((l+h)/2)
        if data[m] == key:
            return m
        else:
            if key < data[m]:
                h = m-1
            else:
                l = m+1
    return None

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binary_search(a, 0))