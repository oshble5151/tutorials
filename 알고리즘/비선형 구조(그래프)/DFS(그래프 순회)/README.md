# DFS

1) 주로 stack 혹은 재귀로 구현한다.(* 재귀가 좀 더 선호된다.)
2) 대부분의 graph는 DFS로 탐색됨
3) 백트래킹 통해 뛰어난 성능을 보임

# 1) DFS 구현(재귀)

재귀를 이용한 DFS가 좀더 간단하며 선호되는 편이다.

다음과 같은 graph가 있을때

![image](https://user-images.githubusercontent.com/73323188/122566376-75772300-d082-11eb-87b2-7ebd35a559ac.png)

출발노드를 key로, 도착 노드를 값으로 갖는 dictionary를 다음과 같이 python으로 생성할 수 있다.


```python
graph : {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3]}
def DFS(v,li = []):
    li.append(v)
    for i in graph[v]:
        if not i in li:
            li = DFS(i,li)
    return li    
>>>
[1, 2, 5, 6, 7, 3, 4]
```

# 2) DFS 구현(스택)



복잡하지만,

보다 직관적이며, 소요시간이 더 길다는 장점이 있다.
