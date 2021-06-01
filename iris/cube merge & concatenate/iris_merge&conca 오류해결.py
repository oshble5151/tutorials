1.merge

1) attribute 미스매치
from iris.experimental.equalise_cubes import equalise_attributes
equalise_attributes(file)


2) Duplicate Cubes => 중복된 동일큐브 merge
file.merge(unique=False)


2.concatate

1) Time Units
from iris.util import unify_time_units

# file1.coord('time').units
  file2.coord('time').units => 통일 해줘야 함

unify_time_units(file)
