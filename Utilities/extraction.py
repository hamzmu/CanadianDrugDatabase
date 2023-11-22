from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
from matplotlib import pyplot as plt # plot images
import cv2 #opencv
import os # folder directory navigation

ocr_model = PaddleOCR(lang='en')
img_path = os.path.join('.', 'drug1.jpg')
result = ocr_model.ocr(img_path)
for res in result:
    print(res[1][0])


