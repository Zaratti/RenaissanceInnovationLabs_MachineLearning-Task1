# RenaissanceInnovationLabs_MachineLearning-Task1
Decoding Scribbles – The Handwriting Recognition Challenge.

## Handwritten Text Recognition
This model uses the easyOCR library to recognise handwritten text from an uploaded text/image/picture.

### Setup Instructions
Here is how to test the model and get inferences for your handwritten texts.

- Clone the repository
     - git clone [the handWriting repo](https://github.com/Zaratti/RenaissanceInnovationLabs_MachineLearning-Task1.git)
     - then use _cd handWriting_ to get into the folder.

- Set up the Jupyter Notebook environment
     - open the writingWork.ipynb, see the imported library's.
     - The tested texts produce the coordinates of the tested text/image(s), the text that is been idntified by the model and the confidence.

- Run the Flask App
     - After setting up the environment, run the Flask app: python app.py in any IDE(I used VS Code).
     -  Start the app.py, and you can access the app result at http://127.0.0.1:5000 in your browser.
     -  Navigate to the templates folder, upload an image containing your handwritten text/scribbles, or use your camera. The app will return the recognised text.


### Usage
Reading the [White Paper](https://github.com/Zaratti/RenaissanceInnovationLabs_MachineLearning-Task1/blob/main/RIL%20Task%201.ipynb) will inform what was intended and what has been achieved.
