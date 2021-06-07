# collections defaultdict

딕셔너리와 관련된 특수한 형태의 컨테이너 자료인 defaultdict는 callable 객체를 인수받아 defalut값을 갖는 dictionary를 생성해준다.

즉 key가 없는 경우의 default값이 자동으로 지정되어 있다.

```python
default_dict = ct.defaultdict(int)
default_dict['a']
>>>
0

default_dict = ct.defaultdict(str)
default_dict['a']
>>>
''

default_dict = ct.defaultdict(list)
>>>
[]

```

# 활용법

__1)존재하지 않는 키에 바로 누적계산 가능__

```python
default_dict = ct.defaultdict(int)
default_dict['a'] +=10
print(default_dict['a'])
>>> 10

