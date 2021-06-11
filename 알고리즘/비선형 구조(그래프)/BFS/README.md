# BFS
BFS는 최단 경로를 찾는 다익스트라 알고리즘에 유용하게 사용된다.

BFS는 큐를 활용해 구현된다.

BFS는 DFS와 달리 재귀로 구현되지 않으며, 큐를 활용해서만 구현된다.


```python

def bfs(v):
  discovered = [v]
  queue = [v]
  while queue:
    v = queue.pop(0)
    for i in graph[v]:
      if w not in discovered:
          discovered.append(w)
          queue.append(w)
  return discovered

>>> bfs(1)
[1, 2, 3, 4, 5, 6, 7] 
```
 
