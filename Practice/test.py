s = "ab"
t = "baab"
map = {}


def solution():
    temp = None
    for i, c in enumerate(t):
        if c in map:
            None
        else:
            map[c] = i
    return map
    # for c in s:
    #     if c in map and temp is None:
    #         temp = map[c]
    #     elif c in map and map[c] > temp:
    #         temp = map[c]
    #     else:
    #         return False
    # return True


print(solution())
