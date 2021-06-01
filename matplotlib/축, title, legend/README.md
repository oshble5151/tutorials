# 축 범위 변경
![image](https://user-images.githubusercontent.com/73323188/120324437-95d47d00-c321-11eb-966c-32e791456b52.png)

__1) x,y 변경__

```python
plt.xlim(-20,20)
plt.xlim(-20,20)
```
__2)x,y 동시 변경__

```python
plt.axis([-20,20,-20,20])
```
![image](https://user-images.githubusercontent.com/73323188/120324500-aab11080-c321-11eb-83a9-47660007b11a.png)

__3)그외 축 옵션__

```python
plt.axis('tight')
plt.axis('equal')
```
![image](https://user-images.githubusercontent.com/73323188/120324785-f794e700-c321-11eb-8e3c-3623d82074c9.png)

여백이 균등하게 그려진다.

__4)title, label__
```python
plt.title("title")
plt.xlabel('x')
plt.ylabel('y')
```
![image](https://user-images.githubusercontent.com/73323188/120326471-b9002c00-c323-11eb-9ee7-d33e91392907.png)

__5) legend(범례)__
```python
for i,j in zip(range(0,60,20),["A","B","C"]):
	plt.plot(x+i,label=j)
	plt.legend()
```
![image](https://user-images.githubusercontent.com/73323188/120327820-2496c900-c325-11eb-905c-e471d1a79bac.png)


