import cv2
from pyzbar.pyzbar import decode
import numpy as np
import base64

def __testBase64(imageAsString: str):
    resultArray = base64.b64decode(imageAsString)
    return BarcodeReader(resultArray)
    

def BarcodeReader(imageBytes: bytes):
   if not isinstance(imageBytes, bytes):
       raise TypeError(f'Expected image to be bytes, received: {type(imageBytes)}')
   
   image = cv2.imdecode(np.frombuffer(imageBytes, dtype=np.uint8), cv2.IMREAD_COLOR)
   
   if image is None:
       raise ValueError('Expected image to be formatted as bytes')
   
   detectedElements = decode(image)
   print(len(detectedElements))
   if not detectedElements:
        raise ValueError('No elements detected')
   returnDict = {}
   for index, element in enumerate(detectedElements):
        returnDict[f'element{index}'] = {'data': str(element.data, encoding='utf-8'), 'type': element.type}
        
   return returnDict