import warnings
warnings.filterwarnings('ignore')
import iris
iris.FUTURE.netcdf_promote = True


def woa_subset(url, bbox=[-179.875, -89.875, 179.875, 89.875], level=None):
    cubes = iris.load_raw(url)
    # TODO: Getting only the OA field for now.
    for idx, cube in enumerate(cubes):
        if 'Objectively analyzed mean fields for' in cube.long_name:
            cube = cubes.pop(idx)
            break

    # Select data subset.
    lon = iris.Constraint(longitude=lambda lon: bbox[0] <= lon <= bbox[2])
    lat = iris.Constraint(latitude=lambda lat: bbox[1] <= lat <= bbox[3])
    if level:
        dep = iris.Constraint(depth=lambda z: z == level)
        cube = cube.extract(lon & lat & dep)
    else:
        cube = cube.extract(lon & lat)

    if cube.ndim >= 3 and cube.shape[0] == 1:  # Squeeze time dimension.
        cube = cube[0, ...]
    return cube


import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


def make_map(projection=ccrs.PlateCarree(), resolution='110m'):
    fig, ax = plt.subplots(figsize=(11, 7),
                           subplot_kw=dict(projection=projection))
    ax.set_global()
    ax.coastlines(resolution=resolution, color='k')
    gl = ax.gridlines(draw_labels=True)
    gl.xlabels_top = gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    ax.add_feature(cfeature.LAND, facecolor='0.75')
    return fig, ax

#ocean = dict(Indian=dict(bbox=[45., -32., 105., -32.]))

level = None
ocean = dict(bbox=[45., -32., 105, -32.])


import numpy as np

from ctd import plot_section
from oceans.colormaps import cm
from matplotlib.ticker import FuncFormatter
from iris.pandas import as_data_frame

var = dict(temp='woa18_decav_t00_01.nc')

for key, value in var.items():
    print(key)
    url = value
    #fname = value.split('/')[-1]
    cube = woa_subset(url, bbox=ocean['bbox'], level=level)
    if cube.ndim > 2:
        cube = cube.collapsed(['latitude'], iris.analysis.MEAN)

    if key == 'temp':
        title = 'Temperature'
        units = r'$^\circ$C'
        #cmap = cm.avhrr
    



    lon = cube.coord(axis='X').points
    lat = cube.coord(axis='Y').points
    df = as_data_frame(cube)
    #if key == 'sal':
    #    df = df.clip(33, 37)  # 27.5, 37.5
    levels = np.arange(df.min().min(), df.max().max(), 0.02)
    df.lon = lon
    df.lat = np.repeat(lat, len(lon))


    fig, ax, cbar = plot_section(df, marker=None,
                                 levels=levels)


print(df.lon)


def km(x, pos):
    if x.is_integer():
        x = int(x)
    return '{} km'.format(x)
km_formatter = FuncFormatter(km)
ax.xaxis.set_major_formatter(km_formatter)


def m(x, pos):
    if x.is_integer():
        x = int(x)
    return '{} m'.format(x)
m_formatter = FuncFormatter(m)
ax.yaxis.set_major_formatter(m_formatter)


ax2 = ax.twiny()
xmin, xmax = ax.get_xlim()[0], ax.get_xlim()[-1]
loc = np.array([xmin, xmax*0.25, xmax*0.5, xmax*0.75, xmax])
labels = [np.percentile(lon, 0), np.percentile(lon, 25), np.percentile(lon, 50), np.percentile(lon, 75),
              np.percentile(lon, 100)]
ax2.set_xticks(loc)
#ax2.set_xticklabels(deg(labels))


projection = ccrs.Orthographic(central_longitude=lon.mean(),
                                   central_latitude=lat.mean())
axin = plt.axes([0.625, 0.1, 0.25, 0.25], projection=projection)
axin.set_global()
axin.add_feature(cfeature.LAND)
axin.coastlines()
axin.plot(df.lon, df.lat, 'r', transform=ccrs.Geodetic())

plt.show()




