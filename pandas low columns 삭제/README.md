## padas 행 및 열 삭제 및 
(*자료는 부경대학교 지오데이터 분석 및 시각화 수업에서 제공받은 자료를 활용 하였다.)

```python
import pandas as pd
df = pd.read_csv('gapminder.tsv',sep='\t')
df
>>>
          country continent  year  lifeExp       pop   gdpPercap
0     Afghanistan      Asia  1952   28.801   8425333  779.445314
1     Afghanistan      Asia  1957   30.332   9240934  820.853030
2     Afghanistan      Asia  1962   31.997  10267083  853.100710
3     Afghanistan      Asia  1967   34.020  11537966  836.197138
4     Afghanistan      Asia  1972   36.088  13079460  739.981106
...           ...       ...   ...      ...       ...         ...
1702     Zimbabwe    Africa  2002   39.989  11926563  672.038623
1703     Zimbabwe    Africa  2007   43.487  12311143  469.709298

[1704 rows x 6 columns]
```
0~3번 까지의 index(행 제거)를 위해 drop함수를 활용한다.
```python
df.drop([0,1,2])
>>>
          country continent  year  lifeExp       pop   gdpPercap
3     Afghanistan      Asia  1967   34.020  11537966  836.197138
4     Afghanistan      Asia  1972   36.088  13079460  739.981106
5     Afghanistan      Asia  1977   38.438  14880372  786.113360
6     Afghanistan      Asia  1982   39.854  12881816  978.011439
7     Afghanistan      Asia  1987   40.822  13867957  852.395945
...           ...       ...   ...      ...       ...         ...
1702     Zimbabwe    Africa  2002   39.989  11926563  672.038623
1703     Zimbabwe    Africa  2007   43.487  12311143  469.709298

[1701 rows x 6 columns]
```
drop(axis=1)을 활용하여 열을 삭제 할 수 있다.

```python
df.drop(['country' ,continent'] , axis=1)
```
iloc(numpy style indexing)을 활용하면 다음과 같이 동일한 결과를 얻을 수 있다.
```python
df.drop(df.iloc[:,0:2], axis=1)
>>>
      year  lifeExp       pop   gdpPercap
0     1952   28.801   8425333  779.445314
1     1957   30.332   9240934  820.853030
2     1962   31.997  10267083  853.100710
3     1967   34.020  11537966  836.197138
4     1972   36.088  13079460  739.981106
...    ...      ...       ...         ...

1702  2002   39.989  11926563  672.038623
1703  2007   43.487  12311143  469.709298
```
```python
df.drop(df.iloc[:,0:2], axis=1,inplace = True)
print(df)
```
inplace를 활용해 df에 drop함수의 결과가 적용됨을 확인 가능하다.
