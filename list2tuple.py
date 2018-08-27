def list2tuple(list, *indexes):
    target = []
    for idx in indexes:
        target.append(list[idx])
    return tuple(target)


mylist = ["F", "E", "D", "E", "R", "I", "C", "O", " ", "M", "E", "S", "T", "R", "O", "N", "E"]

res = list2tuple(mylist, 0, 1, 2, 8, 9, 10, 11, 12)

print(list(res))
