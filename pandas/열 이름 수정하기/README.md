## pandas 열 이름 바꾸기 

판다스의 열을 바꾸는 법에 대해 알아보고자 한다.

판다스 열을 바꾸는 방법은 2가지가 있다.

## .columns attribute를 활용하여 바꾸는 법
```python
df = pd.DataFrame(np.zeros((3,3)))
>>>
   col1  col2  col2
0   0.0   0.0   0.0
1   0.0   0.0   0.0
2   0.0   0.0   0.0

df.columns = ['new_col1','new_col2','new_col3']
>>>
   new_col1  new_col2  new_col3
0       0.0       0.0       0.0
1       0.0       0.0       0.0
2       0.0       0.0       0.0
```
## rename method를 활용하여 바꾸는 법
```python
df.rename(columns = {'col1':'new_col1','col2':'new_col2','col3':'new_col3'}, inplace =1)
>>>
   new_col1  new_col2  new_col2
0       0.0       0.0       0.0
1       0.0       0.0       0.0
2       0.0       0.0       0.0
```
index도 마찬가지로 바꾸어 줄 수있다.
