import iris

file = iris.load_cube('file_name')

file.coord('latitude').guess_bounds()
file.coord('longitude').guess_bounds()

grid_areas = iris.analysis.cartography.area_weights(file)

new_file = file.collapsed(['longitude','latitude'], iris.analysis.MEAN, weights = grid_areas)
