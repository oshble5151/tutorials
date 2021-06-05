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
globals().keys()로 변수가 전역범위에 잘 저장되었는지 확인할수 있다.

```python
globals().keys()
>>>
dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', 'var_name', 'values', 'i', 'j', 'a', 'b', 'c', 'd', 'e'])
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

하지만 load 해야할 자료의 개수가 상당히 많을 경우, 변수의 name과 load할 file_name을 지정해놓고, for문을 활용하여 지정해주는 편이 

더 간편하다. 

netCDF4나 iris를 활용해 많은 개수의 file을 load해야할 경우 다음과 같이 간단하게 for 문을 활용해 load할 수 있다.
```python

name_list = ['atmos_month_%d.nc'%i for i in range(1981,2011)]

for i,j in enumerate(name_list):
      print(j)
      exec("file%d = iris.load_cube(j,'tas')"%(i+1))
```
