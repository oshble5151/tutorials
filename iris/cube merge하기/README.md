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
>>>

