# merge

merge는 scalar 축을 기준으로 다수의 cube를 하나의 cube로 합쳐주는 과정이다.


다음 그림과 같이 3개의 큐브가 time이라는 scalar coordination을 가지고 있을때, 하나의 파일로 합쳐줄수 있다. 

![image](https://user-images.githubusercontent.com/73323188/120179280-52a4dc00-c245-11eb-9b0e-0f0cb466b575.png)

iris의 merge는 각각의 큐브가 가지고 있는 동일한 이름의 scalar coordination을 Dimention coordination으로 바꿔주어 차원을 확장 시켜준다.

다음과 같은 3 큐브를 merge 할수 있다.

```python
import iris
print(file1)
print(file2)
print(file3)
>>>
unknown / (unknown)                 (latitude: 3; longitude: 3)
     Dimension coordinates:
          latitude                           x             -
          longitude                          -             x
     Scalar coordinates:
          time: 48885
          
unknown / (unknown)                 (latitude: 3; longitude: 3)
     Dimension coordinates:
          latitude                           x             -
          longitude                          -             x
     Scalar coordinates:
          time: 48886

unknown / (unknown)                 (latitude: 3; longitude: 3)
     Dimension coordinates:
          latitude                           x             -
          longitude                          -             x
     Scalar coordinates:
          time: 48887
```
3개의 큐브는 같은 name의 scalar 축을 가지고 있고, 이는 cube들의 time scalar coordination은 각각 다른 시간 meta data를 갖고있다.

같은 scalar coordination을 가지고 있지 않은 경우, cube를 merge 시킬 수 없다.

```python
cube_list = iris.cube.Cube([file1, file2, file3])
cube_list.merge()
>>>
[<iris 'Cube' of unknown / (unknown) (-- : 3; latitude: 3; longitude: 3)>]

merge_cube, = cube_list.merge()

print(merge_cube)
>>>
unknown / (unknown)                 (time: 3; latitude: 3; longitude: 3)
     Dimension coordinates:
          time                           x            -             -
          latitude                       -            x             -
          longitude                      -            -             x
```
위와 같이 scalar coordination 이었던 time이 Dimension coordination으로 변환 되었다.

## merge & merge_cube

__1) merge__ 

merge를 수행하면 cube_list에 들어있는 cube 중 merge가 가능한것만 수행되고, 가능하지 않을 경우 그대로 남아있게 된다.

이 예시를 보기 위해, 다음과 같이 scalar 축이 지정 되어있지 않은 cube를 포함시켜 merge 해보려 한다.
```python
print(file4)
>>> 
unknown / (unknown)                 (latitude: 3; longitude: 3)
     Dimension coordinates:
          latitude                           x             -
          longitude                          -             x
    

cube_list2 = iris.cube.Cube([file1, file2, file4])
cube_list2.merge()
>>>
[<iris 'Cube' of unknown / (unknown) (time: 2; latitude: 3; longitude: 3)>,
<iris 'Cube' of unknown / (unknown) (latitude: 3; longitude: 3)>]
```
위와 같이 file1과 file2는 scalar 축이 같으므로 merge되었지만, scalar 축이 없는 file4는 merge되지 않은 것을 확인 할 수 있다.

merge의 결과로 출력된 list에는 병합된것과 되지 않은 것이 모두 요소로서 포함되어있다. 


__2) merge_cube__

merge_cube()는, merge 결과로 나온 list의 요소가 하나일 때만 출력해준다.

즉, merge하려는 cube_list내부의 모든 요소가 merge 가능 할때만 오류가 발생하지 않는다.

```python

cube_list2 = iris.cube.Cube([file1, file2, file4])


cube_list2.merge_cube()
>>>
MergeError: failed to merge into a single cube.
  Coordinates in cube.aux_coords (scalar) differ: time.
```
time scalar축이 없다는 오류가 발생하였다.

이와 같이 merge_cube를 사용하면, merge가 되지 않는 이유를 파악하는데 유용하다.

# concatenate

concatenate는 차원을 증가시키지는 않고, 좌표의 범위를 증가시킨다.

다음 그림과 같이 두 큐브가 연속되는 각각 다른 시간축을 가질 때 , concatenate로 두 큐브로 합쳐 시간축을 확장시켜줄 수 있다.

![image](https://user-images.githubusercontent.com/73323188/120181824-90efca80-c248-11eb-9b0a-c485499f6cd8.png)


```python
repr(a) ; repr(b) ; repr(c)
>>>
"<iris 'Cube' of unknown / (unknown) (time: 3; latitude: 3; longitude: 3)>"
"<iris 'Cube' of unknown / (unknown) (time: 3; latitude: 3; longitude: 3)>"
"<iris 'Cube' of unknown / (unknown) (time: 3; latitude: 3; longitude: 3)>"

file1.coord('time').points
file2.coord('time').points
file3.coord('time').points
>>>
array([48885, 48886, 48887])
array([48888, 48889, 48890])
array([48891, 48892, 48893])  # 각 큐브가 연속된 time 축을 가짐

cube_list = iris.cube.Cube([file1, file2, file3])
cube_list.concatenate()

conca_cube, = cube_list.concatenate()

print(conca_cube)
print(con_cube.coord('time'))
>>>
<iris 'Cube' of unknown / (unknown) (time: 9; latitude: 3; longitude: 3)>
DimCoord(array([48885, 48886, 48887, 48888, 48889, 48890, 48891, 48892, 48893]), ...
```
concatenate와 concatenate_cube의 차이는 merge에서와 같다.

# merge error 발생 해결
merge시 attribute가 동일하지 않은 경우 오류가 발생한다.

```python
cube_list.merge_cube()
>>>
iris.exceptions.MergeError: failed to merge into a single cube.
  cube.attributes values differ for keys: 'history'
```
merge가 아닌 merge_cube()를 써야 오류메시지를 볼 수 있음에 주의해야한다.

이 경우 equalise_attributes를 용하여 merge를 진행 할 수 있다.
```python
from iris.experimental.equalise_cubes import equalise_attributes

equalise_attributes(cubes)
cubes.merge_cube()
```
## iris.experimental.equalise_cubes.equalise_attributes변경
iris.util.equalise_attributes(<cubes>) 로 변경


