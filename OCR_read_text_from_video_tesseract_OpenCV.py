#Using OCR (Tesseract, OpenCV, PIL) to read text from VIDEOS

from PIL import Image
import pytesseract
import os
import cv2

if not os.path.exists('image_frames'):
    os.makedirs('image_frames')

    #Create video parts
    test_vid = cv2.VideoCapture('testvideomp4.mp4')

    #Start index or count for frames
    index = 0

    #Extract "photo" from frames of the video
    while test_vid.isOpened():
        ret, frame = test_vid.read()
        if not ret:
            break

        #Assign a name for our files
        name = './image_frames/frame' + str(index) + '.png'

        #Save files
        print('Extracting frames...' + name)
        cv2.imwrite(name, frame)
        index = index + 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    test_vid.release()
    cv2.destroyAllWindows()

#for el in range(1, 10, 2):

#Open and read some pics from the folder where we previously stored the screenshots from the video
rpics = [5, 10, 15]
for el in rpics:
    demo = Image.open(r'image_frames/frame'  + str(el) + '.png')
    print(el, '...............................................')
    text = pytesseract.image_to_string(demo, lang='eng')
    print(text)