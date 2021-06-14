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
