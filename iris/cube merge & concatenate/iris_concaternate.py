# 3 차원의 큐브끼리 길게 이어 붙일때 사용
# shape, metadata, attributes, coordinates, coordinates metadata, fill value 동일해야함

f1 = iris.load_cube(file_name1) # 3D (60,241,480)
f2 = iris.load_cube(file_name2) # 3D (62,241,480)
f3 = iris.load_cube(file_name3) # 3D (62,241,480)

culi = iris.cube_CubeList([f1,f2,f3])

culi.concaternate_cube()
# error => 
ConcatenateError: failed to concatenate into a single cube.
Cube metadata differs for phenomenon: Total precipitation

#slove => equalise_attributes

from iris.experimental.equalise_cubes import equalise_attributes
equalise_attributes(culi #CubeList_name)
#=> 일치하지 않는 속성들이 삭제 됨




