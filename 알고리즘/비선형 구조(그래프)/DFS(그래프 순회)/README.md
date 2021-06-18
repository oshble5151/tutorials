# DFS

1) 주로 stack 혹은 재귀로 구현한다.(* 재귀가 좀 더 선호된다.)
2) 대부분의 graph는 DFS로 탐색됨
3) 백트래킹 통해 뛰어난 성능을 보임

# DFS 구현(재귀)

다음과 같은 graph가 있을때

![image](https://user-images.githubusercontent.com/73323188/122566376-75772300-d082-11eb-87b2-7ebd35a559ac.png)


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

