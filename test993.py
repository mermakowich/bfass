def count_components(grid):
    m = len(grid)
    n = len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    queue = [(0, 0)]
    visited[0][0] = True

    while queue:
        x, y = queue.pop(0)

        # Проверяем соседей
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y]:
                if grid[new_x][new_y] == '#':
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))

    return sum(sum(visited, [])) // 2  # Делим на 2, так как каждый компонент посещается дважды


# Чтение входных данных
M, N = map(int, input().split())
grid = [list(input()) for _ in range(M)]

# Вывод результата
print(count_components(grid))