## 계절별(JJA,DJF) 자료
data의 자료를 볼때, 계절별로 나누어서 확인해야 할때가 있다.

다음과 같이 대기온도(2m) 자료를 load하고, time 축을 확인한다.
```python
file = iris.load_cube('atmos_month_2001.nc')
file.coord('time')
