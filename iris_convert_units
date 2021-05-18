import iris
f = iris.load_cube('file_name')
f.units = 'mm/day'
f.convert_units('mm/second') # 데이터 값도 함께 변한다.
f.units = 'mm/second'


f.units = 'mm/day'
f.units = 'mm/second' # change directly units => 데이터 값은 변하지 않는다. 


