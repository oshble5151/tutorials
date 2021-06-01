# font
mpl.font_manager.fontManager.ttflist attribute에서 font에 대한 정보를 확인 가능하다. 

__1)font name 확인__
```python
import matplotlib as mpl
set([f.name for i in mpl.font_manager.fontManager.ttflist])
>>>
{'Gill Sans MT', 'Yet R', 'Castellar', 'MS Outlook', 'Niagara Solid', 'Script MT Bold', 'STIXNonUnicode', 
..., 'HYGraphic-Medium', 'Playbill', 'Californian FB'}
```
위와 같이 font의 name을 확인할 수 있다.

__2)fontdict 적용__

fontdict의 구성요소는 다음과 같다.

폰트체와 사이즈, 색상, bold체 등의 변화를 줄 수 있다.

![image](https://user-images.githubusercontent.com/73323188/120332088-5c077480-c329-11eb-9beb-530a8c1724fc.png)

```python
font1= {'family':'Courier New',"size":24,'color':"black"}
font2= {'family':'Lucida Bright',"size":24,'color':"blue",fontweight:'bold'}


for i,j in zip(range(0,60,20),["A","B","C"]):
	plt.plot(x+i,label=j)
	plt.legend()

plt.title('title',fontdict=font1)
plt.xlabel("x",fontdict=font2)
```
![image](https://user-images.githubusercontent.com/73323188/120336484-5ca20a00-c32d-11eb-9452-6dbd36da5eb0.png)
