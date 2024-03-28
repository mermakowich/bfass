n, m = map(int, input().split())
field = {(x, y) for y in range(n) for x, c in enumerate(input()) if c == '#'}


def dfs(xy):
    field.discard(xy)
    x, y = xy
    for ij in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
        if ij in field:
            dfs(ij)


res = 0
while field:
    dfs(field.pop())
    res += 1
print(res)
