from flask import Flask, request, render_template
import easyocr

app = Flask(__name__)

#Initialize the EasyOCR reader (assuming you're using English OCR)
reader = easyocr.Reader(['en'], gpu=False)

# Route to display the OCR page
@app.route('/')
def index():
    return render_template('index.html')

# Route to upload, process an image and send feedback to result page
@app.route('/upload', methods=['POST'])
def handWriting():
    if 'file' not in request.files:
        return render_template('result.html', handwriting_result=['No file uploaded']), 400
    
    file = request.files['file']
    if file.filename == '':
        return render_template('result.html', handwriting_result=['No selected file']), 400
    
    if file:
        # Ensure file is read as bytes
        image_bytes = file.read()  # Read the file as bytes
        # Perform OCR on the uploaded image
        result = reader.readtext(image_bytes, detail=0)  # detail=0 for only text
        # Return HTML with result
        return render_template('result.html', handwriting_result=result)

if __name__ == '__main__':
    app.run(debug=True)