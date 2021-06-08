
본 게시글에서는 iris의 cube를 pandas형태로 변환한뒤, 누락값을 채우고 다시 큐브로 변환해보고자 한다.

# land 온도 누락값 확인

```python
land_temp = iris.load_cube('land_month_1981.nc',t_ref)
>>>
temperature at 2 m over land / (deg_k) (time: 12; latitude: 90; longitude: 144)
     Dimension coordinates:
          time                              x             -              -
          latitude                          -             x              -
          longitude                         -             -              x
     Attributes:
          code_version: $Name: tikal_201409 $
          filename: land_month.tile1.nc
          grid_tile: N/A
          grid_type: regular
          history: /home/gaia/MODEL/WORK/KIOST_AMIP_result/fregrid --input_mosaic /home/gaia/MODEL/WORK/KIOST_AMIP/INPUT/C48_mosaic.nc...
          interp_method: conserve_order1
          time_avg_info: average_T1,average_T2,average_DT
          title: KIOST_ESM_PI-Control-CMIP6
          valid_range: [100. 400.]
     Cell methods:
          mean: time
```
![image](https://user-images.githubusercontent.com/73323188/121143801-65886380-c878-11eb-8ca9-30aba68e4e61.png)

그림과 같이 land 온도(2m)의 자료에는 대기의 영역의 data가 들어가 있지 않고 masking 처리되어있다.

# land 온도의 누락값을 대기온도로 채우기

대기의 자료에는 전지구 격자의 값이 모두 들어가 있으므로, land에서 누락된 data를 대기의 온도값으로 사용하고자 한다.

이 과정을 iris의 cube를 pandas의 DataFrame 형태로 바꿔준뒤, pandas의 fillna method를 사용하여 진행 해보고자 한다.

iris는 iris.pandas module을 제공하여 cube object과 DataFrame을 서로 변환가능하게 해주며, 따라서 pandas의 유용한 method들을 사용할 수 있다.

__1) cube, DataFrame 변환__

```python
land_temp = iris.load_cube('land_month_1981.nc','t_ref')[6] # select july
air_temp = iris.load_cube('atmos_month_1981.nc','tas')[6] # select july

land_temp_dataframe = iris.pandas.as_data_frame(land_temp)
air_temp_dataframe = iris.pandas.as_data_frame(air_temp)

print(land_temp_dataframe)
>>>
               1.25        3.75        6.25        8.75     ...      351.25      353.75      356.25      358.75
-89.494382  218.747559  218.747559  218.747559  218.747559  ...  218.747559  218.747559  218.747559  218.747559
-87.977528  219.594131  219.546707  219.498322  219.448944  ...  219.774033  219.730515  219.686035  219.640564
                                                            ...
 87.977528         NaN         NaN         NaN         NaN  ...         NaN         NaN         NaN         NaN
 89.494382         NaN         NaN         NaN         NaN  ...         NaN         NaN         NaN         NaN

[90 rows x 144 columns]

print(air_temp_dataframe)
>>>
                1.25        3.75        6.25        8.75    ...      351.25      353.75      356.25      358.75
-89.494382  217.488785  217.488785  217.488785  217.488785  ...  217.488785  217.488785  217.488785  217.488785
-87.977528  218.918701  218.838608  218.756866  218.673477  ...  219.222565  219.149078  219.073944  218.997147
                                                            ...  
 87.977528  272.478607  272.473114  272.467499  272.461761  ...  272.499420  272.494385  272.489227  272.483978
 89.494382  272.380524  272.380524  272.380524  272.380524  ...  272.380524  272.380524  272.380524  272.380524

[90 rows x 144 columns]
```
위와 같이 iris.pandas.as_data_frame을 활용하면 cube를 간단하게 DataFrame으로 변환시켜준다.

__2) fillna__ 

DataFrame의 

```python
land_fill_data = land_temp_dataframe.fillna(air_temp_dataframe)

land_fill_cube = iris.pandas.as_cube(land_fill_data)

print(land_fill_cube)

unknown / (unknown)                 (index: 90; columns: 144)
     Dimension coordinates:
          index                           x            -
          columns                         -            x
``` 
iris.pandas.as_cube로 변환해줄경우 축의 long_name이 index와 columns로 지정되어있다.

iris.coord.long_name attribute를 새로 지정하여 축의 이름을 위경도 축으로 바꿔줘야함에 주의해야 한다.

```python

land_fill_cube.coord('index').long_name = 'latitude'
land_fill_cube.coord('columns').long_name = 'longitude'

print(land_fill_cube)
unknown / (unknown)                 (latitude: 90; longitude: 144)
     Dimension coordinates:
          latitude                           x              -
          longitude                          -              x
```
fillna method에 대기온도의 dataFrame을 넣어, land 온도dataframe의 None값을 대기온도 값으로 채워 주었다.

![image](https://user-images.githubusercontent.com/73323188/121183061-a1ceba80-c89e-11eb-9999-6ca4bd629442.png)

plot해보면, 위와 같이 데이터가 채워진 것을 확인할 수 있다.
