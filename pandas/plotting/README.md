# pandas plot 편의성

pandas를 통해 다양한 plot을 그릴수 있다. 몇가지 편의성에 대해 알아보고자 한다.

__1)datetime x축 변환__

pandas의 plot method로 plot 할 경우, index가 datetime일때 x축을 datetime에 맞게 변환하여 출력해준다.

```python
ds = pd.Series(np.random.randn(500), index=pd.date_range("1/1/2000", periods=500))
ds.plot()
plt.show()
```
![image](https://user-images.githubusercontent.com/73323188/121524935-c491d800-ca32-11eb-9e0d-c69681b8decd.png)

__2) coulmns->label__

또한 dataframe의 columns를 label로 plot해준다.
```python
df = pd.DataFrame([[1,2,3],[4,5,6]],columns=list('abc'))
ds.plot()
plt.show()
```
범례는 False로 설정하면 숨길수 있다.

![image](https://user-images.githubusercontent.com/73323188/121526073-040cf400-ca34-11eb-8cbd-12b744c19daa.png)


__3) Plotting 결측값 처리__

Pandas는 누락된 데이터를 포함하는 Data Frames 또는 Series를 플로팅할 때 결측값 그림 유형에 따라 삭제, 제외 또는 채워준다.
 
