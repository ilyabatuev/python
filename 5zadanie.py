src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
for i in src:
    n = 0
    for h in src:
        if i == h:
            n += 1
    if n == 1:
        result.append(i)
print(result)
