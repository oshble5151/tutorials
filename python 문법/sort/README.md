# sort
sort는 배열의 요소를 오름차순으로 정렬하며 존재하는 배열의 요소를 정리하고, None값을 반환한다.
```python
li = [1,3,2,5,4,9,7,8]
li.sort()
print(li)
>>> [1, 2, 3, 4, 5, 7, 8, 9]


li = ['a', 'e', 'd', 'g', 'f', 'b', 'c']
il.sort()
print(li)
>>> ['a', 'b', 'c', 'd', 'e', 'f', 'g']
```

# key 인수

```python
li = ['1_B', '3_A', '1_C', '2_A', '3_C', '3_B', '1_A', '2_C', '2_B']

__1) key 1개, 알파벳을 기준으로 sort
```python
li.sort(key= lambda x : (x.split('_')[1]))
print(li)
>>> ['3_A', '2_A', '1_A', '1_B', '3_B', '2_B', '1_C', '3_C', '2_C']
```
