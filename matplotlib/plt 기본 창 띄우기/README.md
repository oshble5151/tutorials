## matplotlib 창띄우기

maplot의 가장 기본이 되는 figure을 띄워보고자 한다.

## __plt.figure()__
```python
plt.figure()
```
축이 없는 empty figure가 plot된다.

## __plt.subplot(), plt.subplots() 차이__
```python
plt.subplots(2,2,1)
>>>
<matplotlib.axes._subplots.AxesSubplot at 0x7f227fe0fe50>
# 2 by 2에서 첫 번째 그림만 반환됨
```
![image](https://user-images.githubusercontent.com/73323188/120277871-93f1c600-c2ef-11eb-9a3d-00f2094488d1.png)


```python
plt.subplots(2,2)
>>>
(<Figure size 640x480 with 4 Axes>,
 array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f227fc45a10>,
         <matplotlib.axes._subplots.AxesSubplot object at 0x7f227fd0ad10>],
        [<matplotlib.axes._subplots.AxesSubplot object at 0x7f227fc24c50>,
         <matplotlib.axes._subplots.AxesSubplot object at 0x7f227fbe2210>]],
       dtype=object))
 # 2 by 2의 figure들이 한 꺼번에 배열로 반환됨
 ```
![image](https://user-images.githubusercontent.com/73323188/120277811-7d4b6f00-c2ef-11eb-87d2-fe8b52423cef.png)

