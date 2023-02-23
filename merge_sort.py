def merge_sort(n, s):

    if n <= 1 : return

    m = int(n/2)

    l = n-m

    u = s[:m]
    v = s[m:]

    merge_sort(m, u)
    merge_sort(l, v)

    merge(n, m, l, s, u, v)

def merge(n, m, l, s, u, v):
    u.append(float('inf'))
    v.append(float('inf'))

    i = j = 0

    for k in range(n):
        if u[i] < v[j]:
            s[k] = u[i]
            i += 1
        else:
            s[k] = v[j]
            j += 1

s = [6, 8, 2, 20, 3, 1, 15]
merge_sort(7, s)

print(s)