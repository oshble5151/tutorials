# iris save 

iris save 를 이용하면 간단하게 파일을 합칠 수 있다.

```python

import iris

file1 = iris.load_cube('atmos_month_1981.nc','tas')

iris.save(file1, 'test.nc') # save ncfile
```

### 두 변수를 한파일에 넣어서 저장하고 싶은 경우

iris의 cubeList 객체를 save 할 경우, 두 변수가 들어간 파일을 저장할 수 있다.

```python

file1 = iris.load_cube('atmos_month_1981.nc','tas') # variable : 2m air temperature
file2 = iris.load_cube('atmos_month_1981.nc','hcc') # variable : high cloud cover 

cubelist = iris.cube.CubeList([file1,file2])

two_var_file = iris.save(cubelist)
```
생성된 file을 linux의 ncdump 명령어로 확인해보면 다음과 같다.

![image](https://user-images.githubusercontent.com/73323188/122513340-42fb0500-d045-11eb-9863-1149570a4529.png)

위와 같이 2변수가 들어간 것을 확인할 수 있다.
