# Codigo para generar un codigo QR
#Python 3

import qrcode # importamos la libreria qrcode
from PIL import Image # importamos la libreria Image de PIL

cadena = input("Introduce el texto que quieres codificar: ") # pedimos el texto que queremos codificar
imagen = qrcode.make(cadena) # creamos el codigo QR
nombre_img= input("Introduce el nombre de la imagen: ")+".png" # pedimos el nombre de la imagen
archivo_img = open(nombre_img, "wb") # abrimos el archivo en modo escritura binaria
imagen.save(archivo_img) # guardamos el archivo imagen
#archivo_img.close() # cerramos el archivo
ruta_imagen = './' + nombre_img # definimos la ruta de la imagen
Image.open(ruta_imagen).show() # mostramos la imagen