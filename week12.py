from collections import deque

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]       # 무방향 그래프 : 2차원 리스트로 표현했을 때 대칭이다
# DFS : 깊이 우선 탐색
def dfs(g,i,visited):
    visited[i] = True
    print(chr(ord('A')+i),end=" ")
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g,j,visited)

# BFS : 너비 우선 탐색
def bfs(g, i, visited):
    queue = deque([i])
    visited[i] = 1
    # while len(queue) != 0:
    while queue:
        i = queue.popleft()
        print(chr(ord('A')+i), end='')
        for j in range(len(graph)):
            if g[i][j] == 1 and not visited[j]:
                queue.append(j)
                visited[j]=1

visited_dfs = [False for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]
dfs(graph,3,visited_dfs)
bfs(graph,4,visited_bfs)