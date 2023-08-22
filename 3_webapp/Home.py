import streamlit as st 

# Configure Streamlit page settings for the homepage
st.set_page_config(
    page_title="Home",
    layout='wide',
    page_icon='./images/home.png'
)

# Title and description for the homepage
st.title("YOLO V5 Object Detection App")
st.caption('This web application demonstrates Object Detection')

# Content
st.markdown("""
### About this App

Welcome to the YOLO V5 Object Detection App. This application allows you to perform object detection on images using the YOLO (You Only Look Once) V5 model. You can upload an image and the model will automatically detect and highlight various objects present in the image.

To get started, follow these steps:
1. Navigate to the [YOLO_for_image](/YOLO_for_image/) by clicking the link.
2. Upload an image using the provided interface.
3. Click the "Detect Objects" button to run the YOLO model on the image.
4. The app will display the uploaded image with highlighted objects.

### Detected Objects

The YOLO model is capable of detecting a variety of objects. Here are some examples:

1. Person
2. Car
3. Chair
4. Bottle
5. Sofa
6. Bicycle
7. Horse
8. Boat
9. Motorbike
10. Cat
11. TV Monitor
12. Cow
13. Sheep
14. Airplane
15. Train
16. Dining Table
17. Bus
18. Potted Plant
19. Bird
20. Dog

Feel free to explore and have fun with object detection using this app!
""")
