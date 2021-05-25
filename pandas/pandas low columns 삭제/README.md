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
다음 두가지 방법으로 열을 지정하여 삭제 할 수 있다.

```python
df.drop(['country' ,continent'] , axis=1)
df.drop(columns = ['country' ,continent'])
```

iloc(numpy style indexing)를 활용하면 다음과 같이 동일한 결과를 얻을 수 있다.
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
colums attribute를 활용할 수 도 있다.
```python
d.drop(d.columns[0:2],1)
>>>
      year  lifeExp       pop   gdpPercap
0     1952   28.801   8425333  779.445314
1     1957   30.332   9240934  820.853030
2     1962   31.997  10267083  853.100710
3     1967   34.020  11537966  836.197138
4     1972   36.088  13079460  739.981106
...    ...      ...       ...         ...
```
inplace를 활용해 df에 drop함수의 결과가 적용됨을 확인 가능하다.
```python
df.drop(df.iloc[:,0:2], axis=1,inplace = True)
print(df)
```
행에서 특정 조건을 주어 출력하고 싶으면, numpy style의 indexing을 이용할 수 있다.
```python
df[df.year ==1952]
print(df)
>>>
                 country continent  year  lifeExp       pop    gdpPercap
0            Afghanistan      Asia  1952   28.801   8425333   779.445314
12               Albania    Europe  1952   55.230   1282697  1601.056136
24               Algeria    Africa  1952   43.077   9279525  2449.008185

...                  ...       ...   ...      ...       ...          ...
1680              Zambia    Africa  1952   42.038   2672000  1147.388831
1692            Zimbabwe    Africa  1952   48.451   3080907   406.884115

df[df.year >= 2000]
print(df)
>>>
          country continent  year  lifeExp       pop    gdpPercap
10    Afghanistan      Asia  2002   42.129  25268405   726.734055
11    Afghanistan      Asia  2007   43.828  31889923   974.580338
...           ...       ...   ...      ...       ...          ...
1702     Zimbabwe    Africa  2002   39.989  11926563   672.038623
1703     Zimbabwe    Africa  2007   43.487  12311143   469.709298
```
year 조건을 만족하는 data만 나온 것을 확인 할 수 있다.

## indexing 방식 - loc, iloc 
DataFrame에서 indexing을 통해 특정 행, 열의 값에 접근하기 위해서는 다음과 같이 접근해야한다.

country 열에 첫번째 행값에 접근하기 위해서는 
```python
df['country'][0]
>>>
'Afghanistan'
```
loc를 활용하면 다음과 같이 접근 할 수 있다.
```python
df.loc[0,'country']
>>>
'Afghanistan'
```
이와 같이 loc는 [행,열]로 받아들여 indexing 해준다.

DataFrame은 indexing시에 기본적으로 열에 접근 하기 때문에, 위과 같이 접근할 경우 error가 발생한다.
loc는 행의 name을 통해 접근할 수 있게 해준다.
주의해야 하는 점은, loc는 name을 통해 접근하기 때문에 기본 python style과 같이 정수를 활용해 n번째 요소에 접근하는 indexing을 할 수 없다.
```python
df.loc[-1]
>>>
KeyError: -1
```
기본 numpy style(python style)로 indexing 하기 위해서 iloc를 사용할 수 있다.
```python
df.iloc[-1]
>>>
country      Zimbabwe
continent      Africa
year             2007
lifeExp        43.487
pop          12311143
gdpPercap     469.709
Name: 1703, dtype: object
```
다음과 같이 year, lifeExp, pop 열의  0~2번째 행을 추출할 수 있다.
```python
df.iloc[0:3,2:5]
>>>
   year  lifeExp       pop
0  1952   28.801   8425333
1  1957   30.332   9240934
2  1962   31.997  10267083
```
iloc로 행이나 열의 name으로 접근할수 없다.
```python
df.iloc[0:3,'year']
>>>
raise ValueError(
ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types
```









