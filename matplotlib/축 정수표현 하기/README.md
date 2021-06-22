# 축 정보 정수type으로 변환하기
```python
plt.plot([10,20,30,40,50])
plt.show()
```
![image](https://user-images.githubusercontent.com/73323188/122847826-58bd4280-d343-11eb-9364-2aa57bb24c38.png)

x축이 실수로 표현되었다. 축의 정보를 다음과 같이 정수로 나타낼 수 있다.

```python
ax = plt.subplots()
ax[1].plot([1,2,3,4,5])

```
```python
import matplotlib.ticker as ticker
ax = plt.subplots()
ax[1].plot([1,2,3,4,5])
ax[1].xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
```
![image](https://user-images.githubusercontent.com/73323188/122849498-98d1f480-d346-11eb-8c1b-f8f4ed14c9ad.png)

위와 같이 축정보가 정수형으로 변환된 것을 확인 할 수 있다.


