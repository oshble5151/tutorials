# Multi_Indexing
Multi-level indexing은 고차원의 데이터로 작업할 때 정교한 데이터 분석이 가능하게 해준다는 장점이 있다.

Multi-level indexing을 통해서 Series 및 DataFrame과 같은 저차원 데이터 구조에 임의적의 차원과 데이터를 저장하고 조작할 수 있다.

MultiIndex는 grouping, selection, reshape 작업을 수행할 수 있다는 점에서 중요하다.

## Multi_Index 생성 
## __1) tuple로 multi_indexing 생성__ 

multi_index를 가진 카페와 식당의 판매량과 재고량에 대한 간단한 DataFrame을 생성해보고자 한다.
```python
import pandas as pd
index_list = [ ["cafe","cafe", "restraunt", "restraunt"] , ["americano","latte","steak","pasta"] ]
index_mapping = list(zip(*index_list))
print(index_mapping)
>>>
[('cafe', 'americano'), ('cafe', 'latte'), ('restraunt', 'steak'), ('restraunt', 'pasta')]
multi_index = pd.MultiIndex.from_tuples(index_mapping)
print(multi_index)
>>>
MultiIndex([(     'cafe', 'americano'),
            (     'cafe',     'latte'),
            ('restraunt',     'steak'),
            ('restraunt',     'pasta')],)
```
Multi index가 잘 생성되었다.

Multi index을 붙여 DataFrame을 완성하면 다음과 같다.
```python
df = pd.DataFrame(np.random.choice(8,(4,2),replace = 0)
df.columns = 'sale stock'.split(' ')
print(df)
>>>
   sale  stock
0     3      4
1     5      6
2     7      2
3     0      1

df.index = multi_index
print(df)
>>>
                     sale  stock
cafe      americano     3      4
          latte         5      6
restraunt steak         7      2
          pasta         0      1
```
cafe와 restraunt의 정보에 접근할때는 loc를 사용하여 간단하게 접근 할 수 있다.
```python
df.loc['cafe']
>>>
           sale  stock
americano     3      4
latte         5      6

df.loc['restraunt']
>>>
           sale  stock
americano     7      2
latte         0      1
```
mulit_index는 index의 정보를 확실히 하기 위해, index name을 붙여줄 수 있다.

현재 index의 이름을 확인하고, 이름을 새로 지정하고자 한다.
```python
print(df.index.names)
>>>
FrozenList([None, None])
```
현재는 이름이 지정되어 있지 않다. 

names attribute에 이름을 지정해 줄 수 있다.
```python
df.index.names = ['shop','product']

>>>
                     sale  stock
shop      product               
cafe      americano     3      4
          latte         5      6
restraunt steak         7      2
          pasta         0      1
```


## __2) DataFrame으로  multi_indexing 생성__

```python
index_df = index_df = pd.DataFrame({'shop':['cafe','cafe','restraunt','restraunt'], 
                                    'product':['americano','latte','steak','pasta']})

index_from_df = pd.MultiIndex.from_frame(index_df)

df.index = index_from_df
print(df)
>>>
                     sale  stock
shop      product               
cafe      americano     3      4
          latte         5      6
restraunt steak         7      2
          pasta         0      1
```

multi_index는 columns으로도 사용 가능하다.
```python
print(df)
>>>
   0  1  2  3
0  3  5  7  0
1  4  6  2  1

df.index = ['sale','stock']
df.columns = index_from_df
print(df)
>>>
shop         cafe       restraunt      
product americano latte     steak pasta
sale            3     5         7     0
stock           4     6         2     1
```

## 그외 multi_indexing 생성방법

## __1) set_index__

multi_index로 만들어 줄 열을 추가한뒤, set_index로 multiindex를 생성할수 있다.
``` python
df
>>> 
    0   1   2
0   1   2   3
1   4   5   6
2   8   9  10
3  11  12  13

df.insert(0,'multi_index',['x','x','y','y'])  # multi_index로 분류될때 기준이 되는 name이 들어간 열을 추가.
df.insert(1,'type',['A','A','B','B']) # multi_index로 분류될때 기준이 되는 name이 들어간 열을 추가.
>>>
  multi_index type   0   1   2
0           x    A   1   2   3
1           x    A   4   5   6
2           y    B   8   9  10
3           y    B  11  12  13

df = df.set_index(['multi_index','type'])

print(df)
>>>
                   0   1   2
multi_index type
x           A      1   2   3
            A      4   5   6
y           B      8   9  10
            B     11  12  13

print(df.index)
>>>
MultiIndex([('x', 'A'),
            ('x', 'A'),
            ('y', 'B'),
            ('y', 'B')],
           names=['multi_index', 'type'])

```


## __2) concat key__를 활용하여 multi_index 생성

```python

print(df1)
>>>
   0  1  2
0  1  2  3
1  4  5  6
2  7  8  9

print(df2)
>>>
    0   1   2
0  10  20  30
1  40  50  60
2  70  80  90

print(df3)
>>>
     0    1    2
0  100  200  300
1  400  500  600
2  700  800  900

df_new = pd.concat([df1,df2,df3],key = list('xyz'))

>>>
       0    1    2
x 0    1    2    3
  1    4    5    6
  2    7    8    9
y 0   10   20   30
  1   40   50   60
  2   70   80   90
z 0  100  200  300
  1  400  500  600
  2  700  800  900

print(df_new.index)
MultiIndex([('x', 0),
            ('x', 1),
            ('x', 2),
            ('y', 0),
            ('y', 1),
            ('y', 2),
            ('z', 0),
            ('z', 1),
            ('z', 2)],
           )
```
