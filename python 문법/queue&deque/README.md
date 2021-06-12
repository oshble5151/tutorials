# queue
선입선출(FIFO) 방식으로 작동한다.

# deque
앞,뒤 양 방향에서 엘리먼트를 추가하거나 제거할 수 있다.

duque는 양 끝 엘리먼트의 append와 pop의 속도가 queue보다 훨씬 빠르다는 장점이 있다.


# deque 사용법

```python
from collections import deque

deq = deque()
deq.appendleft() # Add element to the start
deq.popleft() #pop element from the start
```

