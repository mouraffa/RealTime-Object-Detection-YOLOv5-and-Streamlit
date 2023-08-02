# Importing necessary libraries
import cv2
from x_yolo_predictions import YOLO_Pred  # Importing the YOLO_Pred class

# Initializing YOLO model with ONNX file and YAML data file
yolo = YOLO_Pred('./Model/weights/best.onnx', 'data.yaml')

# Uncomment to read and display an image for testing
# img = cv2.imread('./test2.jpg')
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Uncomment to run predictions on the image
# img_pred = yolo.predictions(img)

# Capturing video from a file
cap = cv2.VideoCapture('video.mp4')

# Processing the video frames
while True:
    ret, frame = cap.read()  # Reading a frame from the video
    if ret == False:
        print('unable to read video')  # Error message if unable to read the video
