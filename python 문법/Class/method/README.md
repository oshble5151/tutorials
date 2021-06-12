# init  

__init__은 생성과 동시에 instance attribute를 생성해준다.

```python

class test():
  att=1
	def __init__(self):
		self.att=2  # 생성시 에는 att가 2
	def rep(self):
		self.att=0 # rep method를 사용할 경우 att는 0으로 변한다.
  def get(self):
    return self.att  
    
test.att
test().att
>>>
1
2

b = test()
b.rep()
b.att
0
```

__init__을 통해 정적변수(class) 변수를 지정해줄 수 있다.

class test:
       att=0
       def __init__(self):
              test.att+=100

       def rep(self):
              self.att=0

       def get(self):
              return self.att  
test.att
>>> 0

test() # init이 실행되며 att값이 증가함.
test.att
>>> 100
test()
>>> 200



# attribute 은닉

__를 사용하면 외부에서 클래스 attribute에 접근을 차단할 수 있다.

은닉 변수는 __를 붙여 만들며 오직 클래스 내부에서만 사용가능 하다.


# 객체를 함수로 전달

함수내부에서 객체의 attribute를 사용할 수 있다.

```python
obj = test()
def func(obj):
  return obj.att**2

func(obj)
>>>
4
```

# overmethod 

```python
class Car : 
  speed = 0
  def upSpeed(self,value):
    self.speed += value
    
    print(self.speed)
 
class Sedan(Car) : 
  def upSpeed(self,value):
    self.speed += value
    
    if self.speed > 150:
    self.speed=150
```

