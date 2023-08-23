#
import rasterio as rs
import matplotlib.pyplot as plt
import numpy as np
from rasterio import plot
from PIL import Image

img=rs.open("./img/punto_1/planet2020.tif")
#img=rs.open("./img/punto_1/img_sentinel2_2020.tif")

array=img.read().astype('float64')
print(img.meta)
print(img.count)

#-----------
#plot.show(img)

#-----------

red=array[2]
nir=array[3]

print(red)
print(nir)
ndvi=(nir-red)/(nir+red)
print(ndvi)
""" ndviImage = rs.open('./img/ndviImage.tiff', 'w', driver='Gtiff',
                          width=img.width, height=img.height,
                          count=1,
                          crs=img.crs,
                          transform=img.transform,
                          dtype='float64'                  
                         )
ndviImage.write(ndvi,1) #ndvi
ndviImage.close() """

plt.figure(figsize=(10, 10))

plt.imshow(ndvi, cmap='RdYlGn')

plt.colorbar(label='NDVI')

plt.suptitle('NDVI prueba',weight='bold',size=16)

plt.axis('off')
plt.figtext(0.5,0.05,"prueba", bbox = {'facecolor': 'oldlace', 'alpha': 0.5, 'boxstyle': "square,pad=0.3", 'ec': 'black'})
plt.show()



#show(img)