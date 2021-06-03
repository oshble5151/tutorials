# 고해상도에서 저해상도 그리드로 갈때 잘 수행된다.
# 그리드 가중평균으로 계산된다.

# AreaWeighted regridding scheme => 좌표를 경계지어야함
# 경도 및 위도 한계가 정의되지 않은 경우 좌표의 점 값을 기준으로 경계를 추정할 수 있습니다
global_air_temp.coord('longitude').guess_bounds()
global_air_temp.coord('latitude').guess_bounds()

#일정 이하의 값을 마스킹처리 
a = np.ma.array([[1,2,3],[3,2,1],[5,4,3]])
np.ma.masked_less(a,3)
a = [[--, --, 3],
     [3, --, --],
     [5, 4, 3]]
     
     
# mtol
?? 다시 정리하기

# Caching a regridder
rotated_psl = iris.load_cube(iris.sample_data_path('rotated_pole.nc'))
regridder = iris.analysis.Nearest().regridder(f1, f2)

regridder(cube)


     
     
