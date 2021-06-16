# From pdf to png
from pdf2image import convert_from_path

from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)

images = convert_from_path('name.pdf')

for i, image in enumerate(images):
    fname = "image" + str(i) + ".png"
    image.save(fname, "PNG")
