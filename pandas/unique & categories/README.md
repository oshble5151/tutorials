## 1)Unique
unique는 중복되는 값을 제외한 값을 보여준다.

Serise의 Method이며 DataFrame에는 적용되지 않는다.
```python
print(df)
>>>
    name    job
0   Jack   boss
1   Mary  woker
2   Cony   boss
3   Poll  woker
4   Gwen  woker
5  Chris   boss

df.job.unique()
>>>
array(['boss', 'woker'], dtype=object)
```
또한 value_count로 고유한 값이 몇개인지 확인 할 수 있다.
DataFrame에 중복되는 열을 하나 더 추가 한뒤 Seriese와 DataFrame에 value_coutns가 각각 어떻게 적용되는지 확인해보고자 한다.  
```python
df.iloc[-1]=['Jack','boss'] # 마지막 행에 중복되는 열 추가

print(df.value_counts())
print(df.job.value_counts())
>>>
name  job  
Jack  boss     2
Poll  woker    1
Mary  woker    1
Gwen  woker    1
Cony  boss     1
dtype: int64
>>>
woker    3
boss     3
Name: job, dtype: int64
```
DataFrame에서는 모든 열의 값이 같아야 value_counts가 중복값으로 count한다.

## pd.unique
unique는 Series의 method 형태 뿐 아니라 바로 pandas의 함수로 사용가능하다.

인수로는 array, list, Series가 들어갈 수 있다.

```python
pd.unique(df.job)
>>>
array(['boss', 'woker'], dtype=object)
```
결과는 method로서 사용할 때와 같다.

