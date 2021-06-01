# x,y data 쌍을 나열하여 plot
ploting을 다음과 같이 연달아 가능하다.

```python
plt.plot(x1, y1, 'g^', x2, y2, 'g-',x3,y3,'b^')
plt.show()
```
![image](https://user-images.githubusercontent.com/73323188/120279027-ef708380-c2f0-11eb-9a72-b369dbfb2d3f.png)

# **kwargs 언패킹으로 인수 넣기
```python
xarr = np.random.choice(20,(5))
yarr = np.random.choice(20,(5))
plt_dict = {'makers' : 'b','Line Styles' : '-'}
plt.plot(xarr,yarr,**plt_dict)
>>>
```
![image](https://user-images.githubusercontent.com/73323188/120281394-db7a5100-c2f3-11eb-9966-35fc0273e11d.png)

