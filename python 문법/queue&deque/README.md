# queue
선입선출(FIFO) 방식으로 작동한다.

# deque
앞,뒤 양 방향에서 엘리먼트를 추가하거나 제거할 수 있다.

양끝에서 값을 넣고 빼는 데 최적화된 연산속도를 제공하기 때문에, 

duque는 양 끝 엘리먼트의 append와 pop의 속도가 queue보다 훨씬 빠르다는 장점이 있다.


# deque 사용법

```python
from collections import deque

deq = deque()
deq.appendleft() # Add element to the start
deq.popleft() #pop element from the start
```

```python
deq.extendleft([1,2,3,4,5])
>>> deque([5,4,3,2,1])
```
# deque.rotate
```python

deq = deque([1, 2, 3, 4, 5])
deq.rotate(1) # right rotation 
>>>
deq([5,1,2,3,4])
```
