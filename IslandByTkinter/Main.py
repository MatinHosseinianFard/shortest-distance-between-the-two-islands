# from processing_py import *
from Queue import Queue


def solve(mat):
    row = len(mat)
    col = len(mat[0])

    def dfs(i, j, seen):
        if (i, j) in seen or mat[i][j] == 0:
            return
        seen.add((i, j))
        if i - 1 >= 0:
            dfs(i - 1, j, seen)
        if i + 1 < row:
            dfs(i + 1, j, seen)
        if j - 1 >= 0:
            dfs(i, j - 1, seen)
        if j + 1 < col:
            dfs(i, j + 1, seen)

    visited = set()
    for i in range(row):
        if len(visited) > 0:
            break
        for j in range(col):
            if mat[i][j] == 1:
                dfs(i, j, visited)
                break
    q = Queue(10000)
    for land in visited:
        i, j = land
        if i - 1 >= 0 and mat[i - 1][j] == 0:
            q.EnQueue((i - 1, j, 1, i, j))
        if i + 1 < row and mat[i + 1][j] == 0:
            q.EnQueue((i + 1, j, 1, i, j))
        if j - 1 >= 0 and mat[i][j - 1] == 0:
            q.EnQueue((i, j - 1, 1, i, j))
        if j + 1 < col and mat[i][j + 1] == 0:
            q.EnQueue((i, j + 1, 1, i, j))

    while q.Size() > 0:
        i, j, dist, z, x = q.DeQueue()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if mat[i][j] == 1:
            resault = [(z, x), (i, j), dist - 1]
            return resault
        if i - 1 >= 0:
            q.EnQueue((i - 1, j, dist + 1, z, x))
        if i + 1 < row:
            q.EnQueue((i + 1, j, dist + 1, z, x))
        if j - 1 >= 0:
            q.EnQueue((i, j - 1, dist + 1, z, x))
        if j + 1 < col:
            q.EnQueue((i, j + 1, dist + 1, z, x))
