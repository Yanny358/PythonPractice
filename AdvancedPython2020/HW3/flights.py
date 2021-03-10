import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib import pyplot as plt

df1 = pd.read_csv("otselennud.csv")
df2 = pd.read_csv("airports.csv")

merged = df1.merge(df2, on='IATA')
merged.to_csv('flightsFromTLN.csv')

#df3 = pd.read_csv('flightsFromTLN.csv', skiprows=2)

tln_lon = 24.8327999115
tln_lat = 59.41329956049999

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-15, 45, 28, 76], crs=ccrs.PlateCarree())
ax.coastlines(resolution='50m')
ax.add_feature(cfeature.BORDERS.with_scale('50m'))
ax.stock_img()
ax.set_title('Tallinna lennujaama otselennud 2020')

for index, row in merged.iterrows():
    plt.plot([tln_lon, row['Longitude']], [tln_lat, row['Latitude']],
             color='red', linewidth=1, marker='o',
             transform=ccrs.Geodetic(),
             )
    plt.text(row['Longitude'], row['Latitude'], row['IATA'],
             horizontalalignment='right',
             transform=ccrs.Geodetic())

plt.savefig('otselennud2020.png')
plt.show()
