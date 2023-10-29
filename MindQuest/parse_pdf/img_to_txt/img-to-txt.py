import pytesseract
from PIL import Image
import cv2

myconfig = r"--psm 6 --oem 3"
text = pytesseract.image_to_string(Image.open("text.png"), config=myconfig)
print(text)