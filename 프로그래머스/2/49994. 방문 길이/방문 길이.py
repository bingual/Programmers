def solution(dirs):
    n, m = 11, 11
    visited = set()

    def search(y, x):
        d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

        for char in dirs:
            dy, dx = d[char]
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < m:
                visited.add((y, x, ny, nx))
                visited.add((ny, nx, y, x))
                y, x = ny, nx

    search(5, 5)
    return len(visited) // 2