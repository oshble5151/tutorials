# Covariance 공분산

공분산은 2개의 확률변수의 선형관계를 나타낸다. 즉 x가 변할때 y가 변하는 정도를 나타내는 값이다. 

1) 양의 공분산 : x 변수가 증가할 때 y변수도 증가하는 경우, 공분산의 값은 양수

2) 음의 공분산 : x 변수가 증가할 때 y변수는 감소하는 경우, 공분산의 값은 음수

# 공분산 계산
![image](https://user-images.githubusercontent.com/73323188/121827429-e9b66d00-ccf6-11eb-9868-57c459c2a379.png)

E(X) = µ

E(Y) = v

(*E는 평균을 의미)

# pandas cov

cov method를 통해 Series나 DataFrame의 공분산을 계산할 수 있다. 
```python

x=pd.Series([1,2,3,4,5])
y=pd.Series([-30,-10,10,40,70])

x.cov(y)
>>> 62.5
```

# Correlation

상관관계는 두 변수 사이의 관계의 강도를 나타내며, 상관계수에 의해 수치적으로 표현된다.

-1 ~ 1의 범위를 가지며 완전한 양의 상관관계는 1을 의미한다.

상관계수를 구하는 방법은 다음과 같이 3종류가 있다.

## 1) 피어슨 상관 계수 (Pearson correlation coefficient)

변수들간의 관련성을 구하는 이변량 상관분석(bivariate correlation analysis)에서 보편적으로 이용됨.


## 2) 스피어만 상관 계수 (Spearman correlation coefficient)

자료의 값 대신 순위를 이용하는 경우의 상관 계수로서, 데이터를 작은 것부터 차례로 순위를 매겨 서열 순서로 바꾼 뒤 순위를 이용해 상관 계수를 구한다. 두 변수 간의 연관 관계가 있는지 없는지를 밝혀주며 자료에 이상점이 있거나 표본크기가 작을 때 유용하다. 

## 3) 크론바흐 알파 계수 신뢰도 (Cronbach's alpha)

크론바흐 알파(Cronbach's alpha)계수인 신뢰도(reliability) 계수 α는 검사의 내적 일관성 신뢰도를 나타내는 값으로서 한 검사 내에서의 변수들 간의 평균상관관계에 근거해 검사문항들이 동질적인 요소로 구성되어 있는지를 분석하는 것이다. 


# pandas corr

상관계수는 pandas의 corr method를 사용하여 계산할 수 있다.

계산방법의 default값은 피어슨 상관계수 계산법이다.


