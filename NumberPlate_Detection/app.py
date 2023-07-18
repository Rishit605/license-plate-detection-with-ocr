import ocr
import model
import cv2
import numpy as np

# Flask utils
from flask import Flask, request, render_template, jsonify

# Define a flask app
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        
        image = cv2.imdecode(np.frombuffer(f.read(), np.uint8), cv2.IMREAD_COLOR)
        
        results = model.predict(image)
        text = ocr.ocr_text()
        
        ocr.data_tocsv()
        
        return jsonify(text[2]) 

if __name__ == '__main__':
    app.run(debug=True)