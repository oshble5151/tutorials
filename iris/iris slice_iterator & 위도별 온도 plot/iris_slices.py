import iris
f = iris.load_cube('file_name')

slice = f.slices(['latitude','longitude'])

slice_list = list(slice)

#타임 축의 개수만큼 2차원의 큐브로 나누어 진다.
