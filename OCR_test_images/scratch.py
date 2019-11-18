#Using OCR to read text in images

from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


# TESTS ##########################################
#Works well with common type fonts
#demo = Image.open('Developer Salaries in Europe.png')
#demo = Image.open('test_snoopy.png')
#demo = Image.open('pasted image 0.png')
#demo = Image.open('sample_slavs.png')
#demo = Image.open('sample_invoice1.png')
#demo = Image.open('sample_code.png')

#It does not work so well with badly written copy
#demo = Image.open('unnamed.png')
#demo = Image.open('YmulJti.png')
#demo = Image.open("sample_motiv_quote.jpg")

#OPENING AND VIEWING THE FILE
# text = pytesseract.image_to_string(demo, lang='eng')
# print(text)

####################################################

#Save all the pages of a multi-page pdf document
with Img(filename= 'Anexo 2.pdf', resolution = 300) as img:
    img.compression_quality = 99
    img.save(filename = 'image_name_example.jpg')

#Open one of the documents we just saved
demo = Image.open('image_name_example-1.jpg')
text = pytesseract.image_to_string(demo, lang = 'spa')
print(text)

