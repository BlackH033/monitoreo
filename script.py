
import rasterio as rs
import matplotlib.pyplot as plt
import numpy as np
from rasterio import plot

#--------------------------------------------------
#funciones

#ndvi=(nir-red)/(nir+red)
def ndvi(red,nir):
    #ndvi=np.where((nir+red)==0,0,(nir-red)/(nir+red))
    return (nir-red)/(nir+red)

def verdadero_color(r,g,b):
    r=r/r.max()
    g=g/g.max()
    b=b/b.max()
    rgb=np.dstack((r,g,b))
    return rgb

def info(x):
    salida1=f"Pixeles totales: {x.size} | Dimensión: {x.shape} | Valor minimo: {round(np.nanmin(x),3)} | Valor maximo: {round(np.nanmax(x),3)} | Valor promedio: {round(np.nanmean(x),3)}"
    plt.figtext(0.23,0.05,salida1, bbox = {'facecolor': 'oldlace', 'alpha': 0.5, 'boxstyle': "square,pad=0.3", 'ec': 'black'})

def clasificacion(x):
    clases=np.array([-1,0,0.1,0.25,0.4,1])
    ndvi_clasificado=np.digitize(x,clases)
    return ndvi_clasificado


#--------------------------------------------------
#lectura de imagenes

img1=rs.open("./img/punto_1/planet2020.tif")
img2=rs.open("./img/punto_1/img_sentinel2_2021.tif")

#--------------------------------------------------
#sentinel red=0 green=1 blue=2 nir=3
#planet psscene blue=0 green=1 red=2 nir=3
#extracción de bandas 
array_img1=img1.read().astype('float64')
img1_red=array_img1[2]
img1_nir=array_img1[3]
ndvi_img1=ndvi(img1_red,img1_nir)

array_img2=img2.read().astype('float64')
img2_red=array_img2[0]
img2_nir=array_img2[3]
ndvi_img2=ndvi(img2_red,img2_nir)


#-------------------------------------------------- gist_earth gray viridis
#mostrar imagenes bases
fig,((ax1, ax2), (ax3, ax4))=plt.subplots(2,2)

ax1.imshow(verdadero_color(array_img1[2],array_img1[1],array_img1[0]))
ax1.axis("off")
ax1.set_title("2020",fontdict={'weight':'bold'})

ax2.imshow(verdadero_color(array_img2[0],array_img2[1],array_img2[2]))
ax2.axis("off")
ax2.set_title("2021",fontdict={'weight':'bold'})


#mostrar ndvi
plot.show(ndvi_img1,ax=ax3,cmap="RdYlGn",title="NDVI 2020")
ax3.axis("off")
plot.show(ndvi_img2,ax=ax4,cmap="RdYlGn",title="NDVI 2021")
ax4.axis("off")

plt.suptitle("Prueba piloto 01",weight='bold',size=16)
plt.show()

#---------------------------------------------------
#histograma ndvi

fig,((ax1, ax2), (ax3, ax4))=plt.subplots(2,2)
plot.show(ndvi_img1,ax=ax1,cmap="RdYlGn",title="NDVI 2020")
ax2.hist(ndvi_img1.flatten(),label="NDVI",color="green",bins=200)

plot.show(ndvi_img2,ax=ax3,cmap="RdYlGn",title="NDVI 2021")
ax4.hist(ndvi_img2.flatten(),label="NDVI",color="green",bins=200)

plt.suptitle("Prueba piloto 01",weight='bold',size=16)
plt.show()
#---------------------------------------------------
#ndvi individuales
plt.figure(figsize=(10, 10))
plt.imshow(ndvi_img1, cmap='RdYlGn',vmax=1)
plt.colorbar(label='NDVI')
plt.suptitle('Índice de Vegetación de Diferencia Normalizada (NDVI) para 2020',weight='bold',size=16)
plt.axis('off')
info(ndvi_img1)
plt.subplots_adjust(right=0.83)
plt.show()

plt.figure(figsize=(10, 10))
plt.imshow(ndvi_img2, cmap='RdYlGn',vmax=1)
plt.colorbar(label='NDVI')
plt.suptitle('Índice de Vegetación de Diferencia Normalizada (NDVI) para 2021',weight='bold',size=16)
plt.axis('off')
info(ndvi_img2)
plt.subplots_adjust(right=0.83)
plt.show()

#---------------------------------------------------

plt.figure(figsize=(10, 10))
plt.imshow(clasificacion(ndvi_img2), cmap='RdYlGn',vmax=1)
plt.colorbar(label='NDVI')
plt.suptitle('Clasificación NDVI para 2020',weight='bold',size=16)
plt.axis('off')
plt.subplots_adjust(right=0.83)
plt.show()


#--------------------------------------------------

