# Counter 객체

counter는 요소의 개수를 딕셔너리로 표현해준다.
```python
import collections as ct
counter = ct.Counter(['a','a','b','b','b','c','d','d','e','e','e','e','e'])

print(counter)

>>>
Counter({'e': 5, 'b': 3, 'a': 2, 'd': 2, 'c': 1})
```

가장 빈도수가 높은 요소는 most_common을 사용해서 확인가능하다.
```python
counter.most_common(1)
>>>
[('e', 5)]

counter.most_common(2)
>>>
[('e', 5), ('b', 3)]
```

