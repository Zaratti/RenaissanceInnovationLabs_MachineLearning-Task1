# RenaissanceInnovationLabs_MachineLearning-Task1
Decoding Scribbles – The Handwriting Recognition Challenge

## Handwritten Text Recognition
This uses the easyOCR model to recognise handwritten text from an uploaded image.

### Setup Instructions
Here is how to test the model and get inferences for your handwritten texts

- Clone the repository
     - git clone [the handWriting repo](https://github.com/Zaratti/RenaissanceInnovationLabs_MachineLearning-Task1.git)
     - then use _cd handWriting_ to get into the folder

- Set up the environment using Jupyter Notebook
conda env create -f environment.yml conda activate HWR

- Run the Flask App
     - After setting up the environment, run the Flask app: python app.py
     -  This will start the server, and you can access the app at http://127.0.0.1:5000 in your browser.

### Usage
Navigate to the app, upload an image containing your handwritten text/scribbles, or use your camera. The app will return the recognised text.
