# generator

리스트 comprehension을 사용하면, 1에서 100000개의 숫자를 전부 담긴 list를 생성할수 있다.

생성된 10만개의 숫자는 메모리에 전부 할당이 된다.
```python
li = [i for i in range(100000)]
len(li)
>>> 
100000
```

반면 generater를 사용하면, 10만개의 숫자를 만들때 모든 숫자가 메모리에 담기는게 아니라 제너레이터만 생성되고 메모리에 담긴다.

range
```python
def generator(n):
	for i in range(n):
      yield i

generator(100000)
>>>
<generator object a at 0x0000025FA3EF5350>
```

즉, 10만개의 숫자중에서 필요할 때 필요한 숫자만 generator를 사용해서 생성가능하다.

# 기본 사용법

generator는 함수로 작성하고 return yeild를 사용해 구현한다.

기본 함수는 return을 만나면 종료되지만, yeild는 함수를 종료시키지 않고 값을 양보 시킨뒤 이어서 진행한다.

# 할당 memory 비교
```python
li = [i for i in range(100000)]
test_generator = generator(100000)

sys.getsizeof(li)
>>>
824456

sys.getsizeof(test_generator)
>>>
112
```
이과 같이 generator를 활용해 메모리의 점유율을 크게 줄일수 있음을 알수 있다.
