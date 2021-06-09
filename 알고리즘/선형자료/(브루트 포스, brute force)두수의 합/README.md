# 브루트 포스, brute force
  
brute(무식한), force(힘)이라는 뜻으로, __모든 경우의 수를 탐색하는 알고리즘을 말한다.__
 
모든 영역을 전체 탐색하며 __예외 없이 정답만을 추출한다는 장점이 있지만, 시간 복잡도면에서 효율성이 떨어진다.__
 
따라서 브루트 포스는 최적화 시켜줄 필요가 있다.

```python
li =[int(x) for x in list(input('list 입력:').split(','))]
target = int(input('target 입력: '))
for i in range(len(li)):
       for j in range(i+1,len(li)):
              if li[i] + li[j] == target:
                     print([i,j])
```
