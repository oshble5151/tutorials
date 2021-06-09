본 게시글에서는 문자열 뒤집기 문제를 투 포인터 알고리즘으로 풀어보고자 한다.

# 투 포인터(Two Pointer)

투 포인터는 오른쪽과 왼쪽의 포인터가 독자적으로 움직이는며 풀어가는 알고리즘이다.

즉 오른쪽 포인터를 이동하며 답을 찾으면 왼쪽 포인터를 이동시키는 알고리즘이며, 정답이 되지 않는 경우는 제외한다는 특징이 있다.


![image](https://user-images.githubusercontent.com/73323188/121281019-332b4480-c912-11eb-9199-9ffa6aa7e8d9.png)

# 투 포인터를 활용하여  문자열 뒤집기

사실 list의 reverse method를 활용하면 간단하게 문자열을 뒤집을 수 있다.

여기서는 다음과 같이 시작과 끝점에서 투 포인터를 조작해가며 list의 reverse method를 구현해보고자 한다.

![image](https://user-images.githubusercontent.com/73323188/121284650-2e698f00-c918-11eb-8268-3047a5f521eb.png)

```python
string = list(input("입력: "))

pointer1, pointer2 = 0,len(string)-1

while pointer1 < pointer2:
       string[pointer1] ,string[pointer2] = string[pointer2] ,string[pointer1]

       pointer1 +=1
       pointer2 -=1

print("".join(string))
```

```python
입력: Two Pointer
retnioP owT
```
# 주요함수

1) "".join(list object) => 리스트를 요소를 합쳐서 문자열로 변환해줌
```python
t = ['t','e','s','t','_','j','o','i','n']
"".join(t)
```
