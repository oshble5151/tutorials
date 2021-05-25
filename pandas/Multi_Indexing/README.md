## Multi_Indexing
Multi-level indexing은 고차원의 데이터로 작업할 때 정교한 데이터 분석이 가능하게 해준다는 장점이 있다.

Multi-level indexing을 통해서 Series 및 DataFrame과 같은 저차원 데이터 구조에 임의적의 차원과 데이터를 저장하고 조작할 수 있다.


## tuple로 multi_indexing 생성
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
          
