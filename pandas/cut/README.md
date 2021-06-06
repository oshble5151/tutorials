# pandas cut

cut은 연속형 data를 category형으로 변환해준다.

0부터 100사이의 수가 어느 범위에 속하는지 category로 구분 해보려 한다.

```python
print(df)
>>>
   value
0     36
1     91
2     79
3     41
4      0
5     62
6      3
7     40
8     83
9     82
```
다음과 같이 bin으로 범주를 생성하고, label을 사용해 범주의 이름을 설정할 수 있다.
```python

bins =list(range(0,120,20))
label = [str(x)+"<"+"x"+"<" +str(x+20) for x in bins[0:-1]]

df['cartegory']=pd.cut(df[0],bins,right=0,labels=label)

print(df)
>>>
   value cartegory
0     36   20<x<40
1     91  80<x<100
2     79   60<x<80
3     41   40<x<60
4      0    0<x<20
5     62   60<x<80
6      3    0<x<20
7     40   40<x<60
8     83  80<x<100
9     82  80<x<100
```
