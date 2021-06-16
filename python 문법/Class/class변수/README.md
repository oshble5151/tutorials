모든 객체가 공유하는 변수를 class 변수라고 한다.

```python
class test:
      class_att = 0
      def __init__(self,n):
            self.n = n
      def add_class_att(self):
            test.class_att +=1 
      
      def add_self_att(self):
            self.n +=1
            return(self.n)
```

```python
a=test(1)
b=test(2)

a.class_att
>>> 0
b.class_att
>>> 0

b.add_class_att()
b.class_att
>>> 1
a.class_att
>>> 1
```

b에서 증가한 클래스 변수가 a에도 적용된 것을 알 수 있다.

