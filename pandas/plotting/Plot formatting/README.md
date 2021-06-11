본 게시글에서는 pandas의 plot formmating에 대해서 알아보고자 한다.

# Controlling the legend

DataFrame을 plot하면 기본적으로 열의 이름이 legend로 들어간다.

원치않을 경우 False로 제어할 수 있다.

```python
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))

df = df.cumsum()
df.plot(legend=False) # not legend
```
# Controlling the labels
```python
df.plot(xlabel="new x", ylabel="new y")
```

# log Scales 지정
```python 
df.plot(logy=True)
df.plot(logx=True)
```

# secondary axis

```python
ds1
>>>
0    1
1    2
2    3
3    4
4    5
Name: 0, dtype: int32

ds2
>>>
0    500
1    480
2    300
3    380
4    490
Name: 1, dtype: int32
ds1.plot()
ds2.plot()
```
![image](https://user-images.githubusercontent.com/73323188/121621338-f17fd280-caa6-11eb-9bf4-4638a53fc486.png)

위와 같이 y축의 범위가 상당히 떨어진 2개의 data를 plot하면 값이 분포를 보기가 어려운 경우가 있다.

이 경우 second 축으로 구분하여 그려주면 직관적으로 이해하기 수월하다.

```python
ds1.plot()
ds2.plot(secondary_y=True)
```
![image](https://user-images.githubusercontent.com/73323188/121621593-66eba300-caa7-11eb-8b4d-536611d05427.png)

DataFrame을 plot할 경우, second 축에 그릴 열을 지정해줄 수 있다.
```python
df
>>>
   0    1
0  1  500
1  2  480
2  3  300
3  4  380
4  5  490

df.plot()
```
![image](https://user-images.githubusercontent.com/73323188/121621798-d792bf80-caa7-11eb-9b74-f878afab9ec2.png)

B 열만 second 축에 plot된것을 확인할 수 있다.

만일 범례에 right를 표시하고 싶지 않을 경우 , mark_right옵션을 사용하면 된다.
```python
df.plot(secondary_y=["B"], mark_right=False) 
```
