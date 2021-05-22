## pandas data수정

(*자료는 부경대학교 지오데이터 분석 및 시각화 수업에서 제공받은 자료를 활용 하였다.)

pandas는 다양한 방법으로 수정할 수 있다.
```python
print(df)
>>> 
  item  weekdays_order  weekend_order
0    A             500            300
1    B             300            200
2    C             200             50
```
DataFrame은 dict와 같이 바로 data를 추가 가능하다.
```python
df['inventory'] = [1,0,2]
print(df)
>>>
  item  weekdays_order  weekend_order  inventory
0    A             500            300          1
1    B             300            200          0
2    C             200             50          2
```
DataFrame은 df['name']와 같은 방식 외에도, columns attribute로 접근하는 방식이 있다.

columns attribute로 접근해서 data를 수정 할 수 도 있다.
```python
df.item = 'A_new B_new C_new'.split(' ')
>>>
    item  weekdays_order  weekend_order  inventory
0  A_new             500            300          1
1  B_new             300            200          0
2  C_new             200             50          2
```
새로운 열을 추가할때, 기존의 열을 연산하여 값을 추가해 줄 수있다.
```python
df['total'] = df['weekdays_order'] + df['weekend_order']
print(df)
>>>
    item  weekdays_order  weekend_order  inventory  total
0  A_new             500            300          1    800
1  B_new             300            200          0    500
2  C_new             200             50          2    250
```
columns attribute로 접근하는 방식은 data를 수정은 가능하지만, 추가 해 줄수는 없다.

## np.where을 활용한 data 수정
```python
df['inventory'] = np.where(df['item']!= "B_new", 'yes', 'no')
```
## apply method 활용

사용자가 지정한 함수를 apply로 DataFrame에 적용시킬 수 있다.
```python
def test(row):
  if row >= 500:
    return "maintain"
  else:
    return "renewal"
df.total = df.total.apply(test)
print(df)
>>>
    item  weekdays_order  weekend_order  inventory     total
0  A_new             100            300          1  maintain
1  B_new              10            200          0  maintain
2  C_new              10             50          2   renewal
```
total 값이 renewal일 경우, 재주문(reorder)을 해야하는지 여부를 데이터에 추가할 수 있다.

위와 동일한 방법으로 새로운 열을 생성할 수 있다.
```python
def test2(row):
  if row == "maintain":
    return "no"
  else:
    return "yes"
df['reorder'] = df.total.apply(test2)
print(df)
>>>
    item  weekdays_order  weekend_order  inventory     total reorder
0  A_new             100            300          1  maintain      no
1  B_new              10            200          0  maintain      no
2  C_new              10             50          2   renewal     yes
```
