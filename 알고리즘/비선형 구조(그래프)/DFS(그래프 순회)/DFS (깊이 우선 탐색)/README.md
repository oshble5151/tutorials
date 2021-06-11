# DFS

1) 주로 stack 혹은 재귀로 구현한다.(* 재귀가 좀 더 선호된다.)
2) 대부분의 graph는 DFS로 탐색됨
3) 백트래킹 통해 뛰어난 성능을 보임

# DFS 구현(재귀)


graph : {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3]}
```python

def DFS(v,li = []):
    li.append(v)
    for i in graph[v]:
        if not i in li:
            li = DFS(i,li)
    return li    
>>>
[1, 2, 5, 6, 7, 3, 4]
```
