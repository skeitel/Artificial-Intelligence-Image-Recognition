#Using OCR (Tesseract, NLTK) to read text from images

from PIL import Image
import pytesseract

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import pos_tag_sents

# TESTS ##########################################
#Works well with common-type fonts
#demo = Image.open('test_snoopy.png')
#demo = Image.open('sample_slavs.png')
#demo = Image.open('sample_invoice1.png')
#demo = Image.open('sample_code.png')
#demo = Image.open('sample_billboard.png')
# demo = Image.open('pasted image 0.png')
# demo = Image.open('Developer Salaries in Europe.png')

#It does not work so well with badly written copy
#demo = Image.open('unnamed.png')
#demo = Image.open('YmulJti.png')
#demo = Image.open("sample_motiv_quote.jpg")

#OPENING AND VIEWING THE FILE
# text = pytesseract.image_to_string(demo, lang='eng')
# print(text)

#TIPS TO IMPROVE OCR ACCURACY
#Proofread docs before scanning
#Play with black and white
#Play with rotations
#Play eliminating borders
#Condense or stretch images
#Explore libraries' ways to deal with noise
#Select lossless output format like .TIFF
#Scan at 600 dpi instead of 300
#Enhance contrast
#Increase text size
#Select languages contained in source languages
#https://www.youtube.com/watch?v=KS1gd5yUmKo

####################################################
#This did not work as Wand created compatibility problems
# #Save all the pages of a multi-page pdf document
# with Img(filename= 'Anexo 2.pdf', resolution = 300) as img:
#from wand.image import Image as Img
#     img.compression_quality = 99
#     img.save(filename = 'image_name_example.jpg')


#Open and print image
demo = Image.open('OCR_test_images/pasted image 0.png')
text = pytesseract.image_to_string(demo, lang = 'eng')
print(text)
print('+' * 50)


#Preprocess data with NLTK to get POS
example = text
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag_sents(sent)
    return sent
sent = preprocess(example)
print(sent)
print('+' * 50)


#Check if a certain piece of text is in the file
with open('OCR_test_images/foreign_document.txt', 'a') as ftext:
    print(ftext)
    print('+' * 50)


#Check that a certain sentence is in the file
with open('OCR_test_images/foreign_document.txt', 'a') as ftext:
    if 'benefit us' in open('foreign_document.txt').read():
        print('True')


#Using Google library to translate our text with Google API
#https://py-googletrans.readthedocs.io/en/latest/
from googletrans import Translator
with open(r'OCR_test_images/foreign_document.txt', 'r') as ftext:
    new_text = ftext.read()
    translator = Translator()
    translated_text = translator.translate(new_text, src='fr', dest='en')
    #print(translated_text) #translated object
    print('+' * 50)
    print(translated_text.origin)
    print('+' * 50)
    print(translated_text.text)
