from flask import Flask, render_template, request, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        if 'image' not in request.files:
            print('No file part')
            return redirect(request.url)
        image = request.files['image']
        question = request.form.get('question', '')
        if image.filename == '':
            print('No selected file')
            return redirect(request.url)
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
            image_url = url_for('uploaded_file', filename=filename)
            # Print received question for debugging
            print("Received question:", question)
            prediction = "Dummy prediction result"  # Replace with your model's prediction logic
            return render_template('result.html', image_url=image_url, question=question, prediction=prediction)
        else:
            # If the file is not allowed, you can redirect to the upload page with a message
            print('File type not allowed')
            return redirect(request.url)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0',port=5001