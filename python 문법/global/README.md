# global은 함수 내부에서, local space가 아닌 global space에 변수를 지정한다는 의미다.
```python
a=100
def func():
  global a
  a=20
  print(a)
func()
print(a)
```
즉 global을 사용하면 함수 내부에서 전역변수를 건드릴 수 있다.

기본적으로 함수 내부에서 지정된 변수가 아닌 변수를 호출한다면 전역변수에서 호출한다. 

  
