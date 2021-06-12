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

```python
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
```


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

a.upSpeed(200)
b.upSpeed(200)
>>> 200
>>> 150
```

# super method

```python
# using super calss attribute
class super_class():
       def __init__(self):
              self.x = 1

class sub_class(super_class):

       def __init__(self):
              self.y = 2

test = sub_class()
test.x # raise error


class sub_class(super_class):

       def __init__(self):
              super().__init__()
              self.y = 2
test= sub_class()
>>> test.x
1
>>> test.y
2

### 
class super_class():
       def __init__(self,x):
              self.x = 10 + x 

class sub_class(super_class):

       def __init__(self):
              super().__init__(1)
              self.y = 2

```

# super.__init__() 사용하지 않아도 되는 경우 => __init__이 없을 경우
```python              
class super_class():
       def __init__(self):
              self.x = 1 

class sub_class(super_class):

       x= 10

test = sub_class()

sub_class.x
>>> 10

test.x
>>> 1
```





# 오버라이딩 시 super의 메서드 사용 

```python
class super_class():
       def me1(self):
              print('me1') 

class sub_class(super_class):
       def me1(self):
              super.me1()  # => output:'me1'
              print('me2') # => output:'me2'
```
