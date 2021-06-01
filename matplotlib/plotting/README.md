# x,y data 쌍을 나열하여 plot
ploting을 다음과 같이 연달아 가능하다.

```python
plt.plot(x1, y1, 'g^', x2, y2, 'g-',x3,y3,'b^')
plt.show()
```
![image](https://user-images.githubusercontent.com/73323188/120279027-ef708380-c2f0-11eb-9a72-b369dbfb2d3f.png)

# **kwargs 언패킹으로 인수 넣기

plot의 kwargs은 다음과 같은 것들이 존재한다.

![image](https://user-images.githubusercontent.com/73323188/120281720-3f047e80-c2f4-11eb-82c5-78b0bcfb9dde.png)

다음과 같이 **을 사용하여 unpacking하여 함수에 인수로 전달 할수 있다. 
```python
xarr = np.random.choice(20,(5))
yarr = np.random.choice(20,(5))
plt_dict = {'marker' : 'o','linestyle' : '-','linewidth' : '10'}
plt.plot(xarr,yarr,**plt_dict)
>>>
```
![image](https://user-images.githubusercontent.com/73323188/120281394-db7a5100-c2f3-11eb-9966-35fc0273e11d.png)

