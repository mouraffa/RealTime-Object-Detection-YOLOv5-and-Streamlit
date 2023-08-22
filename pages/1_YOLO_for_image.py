import streamlit as st
from yolo_predictions import YOLO_Pred
from PIL import Image
import numpy as np

# Configure Streamlit page settings
st.set_page_config(
    page_title="YOLO Object Detection",
    layout="wide",
    page_icon="./images/object.png"
)

# Display title and introduction
st.title("Welcome to YOLO for Image")
st.write("Please upload an image to perform object detection.")

# Load YOLO model during app initialization
with st.spinner("Please wait while the model is loading..."):
    yolo_model = YOLO_Pred(onnx_model='./models/best.onnx', data_yaml='./models/data.yaml')
    ##st.balloons()

# Function to upload image
def upload_image():
    """
    Function to upload an image using Streamlit's file uploader.
    Validates the image file type and provides details.

    Returns:
        dict: Dictionary containing uploaded image file and its details.
              None if the uploaded file is not valid.
    """
    uploaded_file = st.file_uploader(label='Upload Image')
    if uploaded_file is not None:
        # Calculate file size in MB
        file_size_mb = uploaded_file.size / (1024 ** 2)
        file_info = {
            "filename": uploaded_file.name,
            "filetype": uploaded_file.type,
            "filesize": "{:,.2f} MB".format(file_size_mb)
        }
        st.json(file_info)

        # Validate file type
        if uploaded_file.type in ('image/png', 'image/jpeg'):
            st.success('VALID IMAGE file type (png or jpeg)')
            return {"file": uploaded_file, "details": file_info}
        else:
            st.error('INVALID Image file type')
            st.error('Upload only png, jpg, jpeg, jfif')
            return None

# Main function to run the app
def main():
    """
    Main function to create the Streamlit app interface and control logic.
    """
    uploaded_object = upload_image()

    if uploaded_object:
        prediction_available = False
        uploaded_image = Image.open(uploaded_object['file'])
        
        # Split the layout into two columns for displaying image and details
        col_preview, col_details = st.columns(2)

        # Display image preview in the first column
        with col_preview:
            st.info('Preview of uploaded image')
            st.image(uploaded_image)

        # Display file details in the second column
        with col_details:
            st.subheader('File Details')
            st.json(uploaded_object['details'])
            detect_button = st.button("Detect Objects with YOLO")
            
            if detect_button:
                with st.spinner("Detecting objects in the image. Please wait..."):
                    # Convert image to array for prediction
                    image_array = np.array(uploaded_image)
                    predicted_image = yolo_model.predictions(image_array)
                    predicted_image_obj = Image.fromarray(predicted_image)
                    prediction_available = True
        
        if prediction_available:
            st.subheader("Predicted Image")
            st.caption("Object Detection using YOLO V5 model")
            st.image(predicted_image_obj)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
