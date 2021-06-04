# for문 내부에서의 변수를 생성
미리 생성된 변수를 for문 내부에서 사용하는 것 뿐만 아니라, for문 안에서 loop를 돌며 값을 지정할 수 있다.

__1) globals() dictionary 활용__

__globals()는 전역변수의 name과 값을 각각 key와 value로 가지고 있는 dictionary 이다.__

```python

var_name = list('abcde')

values=[1,2,3,4,5]

for i,j in zip(var_name,values):
        globals()[i] = j

print(a,b,c,d,e)
>>> 
1 2 3 4 5
```

__2) exec 활용__

__exec은 문자열 그래도 선언해주는 함수이다.__

```python
for i ,j in zip(var_name,values):
	exec(i+"=+j")
  
print(a,b,c,d,e)
>>> 
1 2 3 4 5
```

변수의 개수가 적을때는 굳이 반복문안에서 선언 할 필요가 없다.

하지만 불러야할 전지구 자료의 개수가 상당히 많을 경우, 변수의 name과 load할 file_name을 지정해놓고, for문을 활용하여 지정해주는 편이 

더 간편하다.
