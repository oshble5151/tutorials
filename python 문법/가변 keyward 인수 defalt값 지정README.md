# kwargs인수

키워드인수(kwargs)는 키워드를 사용하여, 함수의 인수를 지정해 줄수 있는 방법이다.

함수를 작성할때 **를 붙여 가변키워드인수를 입력하도록 작성할수 있다.

```python
def func(**kwargs):
    print(locals())

func()
>>>
{'kwargs': {}}

func(x=1,y=2,z=3)
>>>
{'kwargs': {'x': 1, 'y': 2, 'z': 3}}
```
**를 매개변수 앞에 붙여주면, 해당 매개변수은 dict 형태로 함수의 지역변수에 저장된다.

# kwargs default값 지정하기

함수를 다음과 같이 수정하고, 필요한 인수를 지정해주지 않을 경우 어떻게 될까.
```python
def func(**kwargs):
	print(locals())
	print(kwargs['x'],kwargs['y'],kwargs['z'])
func(x=1,y=2)
>>>
...
KeyError: 'z'
```
가변 kewargs인수 x,y,z의 값을 print하는 인수에서, z값이 정해져있지 않아 오류가 발생하였다.

가변인수의 값을 지정하지 않아도, default값을 지정해주려면 다음과 같다.

```python
def func(**kwargs):
    if  not kwargs.__contains__('x'):
        kwargs['x'] = None
    if  not kwargs.__contains__('y'):
        kwargs['y'] = None
    if  not kwargs.__contains__('z'):
        kwargs['z'] = None

    print(kwargs['x'],kwargs['y'],kwargs['z'])
func(x=1,y=2)
>>>
1 2 None
```
z값에 default값으로 None 값이 지정되었다.
