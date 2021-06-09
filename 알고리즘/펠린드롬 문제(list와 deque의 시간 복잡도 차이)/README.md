# 1) 펠린드롬(회문) -> list를 활용한 풀이
펠린드롬: 뒤집었을 때 같은 말이 되는것. 

```python
string = input('입력: ')

str_list=[]

for i in string:  # 문자열 전처리=> 알파벳과 숫자가 아닌 것은 포함시키지 않음
  if i.isalnum():
    str_list.append(i.upper())

check_pelin=0

while len(str_list)>1:      
  if str_list.pop(0) != str_list.pop():
    check_pelin+=1

if check_pelin==0:
       print(True)
else: print(False)
```
```python
입력: as, ,, ,dsa  qw wq,a,s,dsa
True

입력: apple
False

```
# 2) 펠린드롬 -> deque를 활용한 풀이
```python
import collections as ct
string = input('입력: ')
str_deque = ct.deque()


for i in string:
  if i.isalnum():
    str_deque.append(i.upper())

check_pelin=0

while len(str_deque)>1:
  print(str_deque)
  if str_deque.popleft() != str_deque.pop():
    check_pelin+=1

if check_pelin==0:
       print(True)
else: print(False)
```


while len(str_list)>1 대신에 while str_list !=[] 로 코딩했더니 오류가 발생하였다.

if str_list.pop(0) != str_list.pop() => 해당 조건문이 실행되기 위해서는 최소 2개의 요소가 필요하다.

따라서 len(str_list)>1 조건을 사용하여 str_list의 요소가 1개 일때는 while문이 돌지 않도록 코드를 짜야한다. 
