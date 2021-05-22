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

columns attribute로 접근해서 data를 추가 할 수 도 있다.
```python
df.item = 'A_new B_new C_new'.split(' ')
>>>
    item  weekdays_order  weekend_order  inventory
0  A_new             500            300          1
1  B_new             300            200          0
2  C_new             200             50          2
```
