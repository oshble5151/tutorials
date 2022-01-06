
```python

test.coord('time').metadata

DimCoordMetadata(standard_name=None, long_name='time', var_name='time', units=None, attributes={'calendar_type': 'JULIAN', 'cartesian_axis': 'T'}, coord_system=None, climatological=False, circular=False)
test.coord('time').metadata = test.coord('time').metadata._replace(standard_name=None, units=None)
```

``` python
Cube.add_dim_coord
Cube.add_aux_coord
Cube.remove_coord

