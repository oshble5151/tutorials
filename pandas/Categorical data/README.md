# Categorical data

범주형 변수는 제한된 수의 가능한 값을 사용한다.

성별, 사회계층,  관찰시간등이 예이다.

범주형 데이터는 순서가 있을 수 있지만, 숫자 연산은 불가능하다.

순서는 값의 어휘 순서가 아니라 범주 순서로 정의됩니다.

내부적으로 데이터 구조는 범주 배열과 범주 배열의 실제 값을 가리키는 정수 배열로 구성된다.

data와 data의 범주를 입력하여 pd.Categorical 객체를 만들 수 있다.  
```python
category = pd.Categorical(["a","b","c","d","e"],categories=["a","c"])
print(category)
>>>
['a', NaN, 'c', NaN, NaN]
Categories (2, object): ['a', 'c']
```
data배열로 a,b,c,d,e가 들어갔고, 이 중에서 지정한 범주인 'a'와 'c'만 값으로 남고 나머지는 None값으로 처리되었다.

```
