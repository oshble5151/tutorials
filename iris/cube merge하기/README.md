# merge

merge는 scalar 축을 기준으로 다수의 cube를 하나의 cube로 합쳐주는 과정이다.

iris의 merge는 동일한 이름의 scalar coordination을 기준으로 cube를 합쳐준다.

다음 그림과 같이 3개의 큐브가 time이라는 scalar coordination을 가지고 있을때, 하나의 파일로 합쳐줄수 있다. 

merge를 수행하면, 큐브병합의 기준이 되는 scalar coordination이 Dimensoin coordinayion이 되어 차원이

![image](https://user-images.githubusercontent.com/73323188/120138542-a1d11980-c211-11eb-8dda-fd83eddaf25e.png)

다음과 같은 3 큐브를 merge 할수 있다.

```python
import iris
print(a)
print(b)
print(c)
>>>
unknown / (unknown)                 (latitude: 3; longitude: 3)
     Dimension coordinates:
          latitude                           x             -
          longitude                          -             x
     Scalar coordinates:
          time: 2021-05-31
          
unknown / (unknown)                 (latitude: 3; longitude: 3)
     Dimension coordinates:
          latitude                           x             -
          longitude                          -             x
     Scalar coordinates:
          time: 2021-06-01

unknown / (unknown)                 (latitude: 3; longitude: 3)
     Dimension coordinates:
          latitude                           x             -
          longitude                          -             x
     Scalar coordinates:
          time: 2021-06-02
```
3개의 큐브는 같은 name의 scalar 축을 가지고 있고, 이는 cube들의 time scalar coordination은 각각 다른 시간 meta data를 갖고있다.

같은 scalar coordination을 가지고 있지 않은 경우, cube를 merge 시킬 수 없다.

```python
cube_list = iris.cube.Cube([a,b,c])
cube_list.merge()
>>>
[<iris 'Cube' of unknown / (unknown) (-- : 3; latitude: 3; longitude: 3)>]

merge_cube, = cube_list.merge()

print(merge_cube)
>>>
unknown / (unknown)                 (-- : 3; latitude: 3; longitude: 3)
     Dimension coordinates:
          latitude                      -            x             -
          longitude                     -            -             x
     Auxiliary coordinates:
          time                          x            -             -
```


