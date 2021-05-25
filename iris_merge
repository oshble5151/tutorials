# scalra coold => merge는 scalra coold를 쌓아서 작업 수행
monotonic sequences 로 결합 가능한 스칼라 좌표가 있어야함.
# shape, metadata, attributes, coordinates, coordinates metadata, fill value 동일해야함
f1  iris.load_cube()

#scalar 좌표 생성 => AuxCoord에 단일 값을 추가하면 됨.
scalar_coord = iris.coords.AuxCoord(1, long_name='name', units='no_unit')

# collapsed => scalar coordinate가 자동 생성됨
test = cube.collpased(['longitude','latitude'])

print(_)
Scalar coordinates:
  latitude: 0.0 degrees, bound=(-90.0, 90.0) degrees
  longitude: 180.0 degrees, bound=(0.0, 360.0) degrees

test = cube.collpased(['time'])
print(_)

Scalar coordinates:
  time: 1986-06-16 06:00:00, bound=(1986-06-01 12:00:00, 1986-07-01 00:00:00)


f1.collapsed('time')

# error =>
MergeError: failed to merge into a single cube. 
cube.attributes values differ for keys: 'history'

#slove 
del f1.attributes['history'] , f2.attributes['history'] , f3.attributes['history']

# error =>
MergeError: failed to merge into a single cube.
Coordinates in cube.aux_coords (scalar) differ: time.

#slove
f1.coord('time').var_name = 'var_name'
f2.coord('time').var_name = 'var_name'
f3.coord('time').var_name = 'var_name'



merge() & merge_cube() 차이

#merge() => 되는 것만 merge
#merge() => 하나라도 merge 안되면 error => 왜 merge안되는지 확인 가능

