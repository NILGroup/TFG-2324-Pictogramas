from os import listdir
from os.path import join
from PIL import Image

imageDir = r"D:\TFG\PodMan\SubDatasets\Palitos2"
outDir = r"D:\TFG\PodMan\SubDatasets\Palitos"

for file in listdir(imageDir):
    if not file.endswith(".png"):
        continue
    filePath =  join(imageDir, file)
    outputPath = join(outDir, file)
    # Carga la imagen de paleta con transparencia
   
    # Carga la imagen de paleta con transparencia
    image_paleta = Image.open(filePath)

    # Convierte la imagen a RGBA
    image_rgba = image_paleta.convert("RGBA")

    # Guarda la nueva imagen RGBA
    image_rgba.save(outputPath)

