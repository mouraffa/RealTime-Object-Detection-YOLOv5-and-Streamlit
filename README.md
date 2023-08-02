# RealTime-Object-Detection-YOLOv5
Comprehensive object detection using YOLOv5, trained from scratch. Includes data preparation, YOLOv5 training on 20 labels, and testing on images/videos. Utilizes Google Colab's V100 GPU for robust detection.


## Usage

### Data Preparation

Open `01. Data_Preparation.ipynb` in Jupyter Notebook and follow the instructions to prepare the data.

### Training the YOLO Model

Open `02. YOLO_training.ipynb` in Google Colab and follow the instructions to train the model.

### Making Predictions

Use the `YOLO_Pred` class from `03. yolo_predictions.py` to make predictions on images or videos.

### Testing

Run `04. test_for_images_and_videos.py` to test the predictions on specific images or videos.

## Test Results

Below are some examples of test results, demonstrating original images and corresponding images with predictions:

- **Original Image 1**: ![Original Image 1](path/to/original_image1.png)
- **Prediction Image 1**: ![Prediction Image 1](path/to/prediction_image1.png)

- **Original Image 2**: ![Original Image 2](path/to/original_image2.png)
- **Prediction Image 2**: ![Prediction Image 2](path/to/prediction_image2.png)

(Add more images as needed)

## Contributing

Feel free to contribute by submitting pull requests or opening issues.

## License

[MIT License](LICENSE)

