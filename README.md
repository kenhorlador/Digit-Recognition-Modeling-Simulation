# Real-time Handwritten Digit Recognition System

## Overview

This application provides a user-friendly interface for real-time handwritten digit recognition. Users can draw a digit on the canvas, and the system will predict the drawn digit with its probability. This project leverages the power of machine learning, specifically a Convolutional Neural Network (CNN) trained on the MNIST dataset, and combines it with the interactive capabilities of Streamlit and OpenCV for an engaging user experience.

## Features

*   **Interactive Canvas:** Users can draw digits directly on the canvas using their mouse or touchscreen.
*   **Real-time Prediction:** The system provides instant predictions as the user draws.
*   **Probability Display:** A bar graph displays the probabilities of the predicted digit, offering insights into the model's confidence.
*   **Streamlit Integration:** The user interface is built using Streamlit, providing a seamless and responsive experience.

## Technical Details

### 1. Machine Learning Model

*   A CNN model is trained on the MNIST dataset, a large collection of handwritten digits.
*   The model architecture consists of convolutional layers to extract features, max-pooling layers to reduce dimensionality, and fully connected layers for classification.
*   The trained model is saved as a `.h5` file for efficient loading and prediction within the application.

### 2. Image Processing with OpenCV

*   OpenCV is used to capture the user's input from the canvas.
*   The drawn image is preprocessed, including resizing, grayscaling, and normalization, to ensure compatibility with the trained model.

### 3. Streamlit for User Interface

*   Streamlit is used to create the interactive web application.
*   The UI includes a canvas for drawing, a display area for predictions, and a bar graph to visualize probabilities.

## Installation and Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/kashishg0004/Offline-Digit-Recognition-System.git](https://github.com/kashishg0004/Offline-Digit-Recognition-System.git)
    ```

2.  **Install dependencies:**
    ```bash
    pip install streamlit opencv-python tensorflow numpy pandas
    ```
    (Make sure to install `protobuf<=3.20.*` if you encounter compatibility issues.)

3.  **Run the application:**
    ```bash
    streamlit run dicpy.py
    ```

4.  **Access in browser:** Open `http://localhost:8501` in your web browser.

5.  **Draw a digit:**  Try drawing a number on the canvas.

## File Structure

*   `dicpy.py`: Main Python file containing the Streamlit application code.
*   `model.h5`: Trained machine learning model file.
*   `notebook.ipynb`: Jupyter notebook used for model training and experimentation (optional).

## Contributing

Contributions are welcome! Feel free to submit pull requests for bug fixes, improvements, or new features.

## License

This project is licensed under the MIT License.

## Acknowledgements

*   The MNIST dataset for providing the training data.
*   The developers of TensorFlow, Streamlit, and OpenCV for their powerful libraries.
