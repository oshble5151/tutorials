# bar

레이블이 지정된 비 시계열 데이터의 경우, bar를 plot할 수 있다.

dataframe으로 bar를 plot할 경우 각각의 index를 기준으로, 열의 값을 비교해준다.

예를들어 5명의 학생의 4가지 과목의 성적을 bar를 통해 다음과 같이 확인 할수 있다.
```python
df = pd.DataFrame(np.random.choice(np.arange(50,100,5),(5,4)), index=['Tom','Jack','Mary','Ann','Jeny'],columns=["Math", "English", "Science","Ethics"])
print(df)
>>>
      Math  English  Science  Ethics
Tom     70       55       65      50
Jack    85       55       50      70
Mary    60       85       70      50
Ann     55       60       60      85
Jeny    65       95       80      95

df.plot.bar()
plt.show()
```
![image](https://user-images.githubusercontent.com/73323188/121527881-dcb72680-ca35-11eb-96c8-9f5b73917a11.png)
 
