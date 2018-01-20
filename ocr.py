# import the necessary packages
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract' # fixes File Not Found Error
# https://stackoverflow.com/questions/31217647/error-using-pytesser-winerror-2-the-system-cannot-find-the-file-specified
import argparse
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", gray)

# check to see if we should apply thresholding to preprocess the image
if args["preprocess"] == "thresh":
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove noise
elif args["preprocess"] == "blur":
    gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temp file so we can apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete the temp file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print (text)
### Next step: Output text to text document

# resize the images to fit on the screen
### Work on resizing to a specific size for all images
newX, newY = int(image.shape[1]/8), int(image.shape[0]/8) #new size(w,h)
resizedImage = cv2.resize(image, (newX, newY) )
resizedGray = cv2.resize(gray, (newX, newY) )

# show the output images
cv2.imshow("Image", image)
cv2.imshow("Output", gray)

#cv2.imshow("Image", resizedImage)
#cv2.imshow("Output", resizedGray)

# wait until a key is pressed
cv2.waitKey(0)
