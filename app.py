from flask import Flask, render_template, request, redirect, url_for,send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        image = request.files['image']
        question = request.form['question']
        if image:
            filename = image.filename
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
            # Ensure the filename is safe to use in a URL
            # Flask's secure_filename function can be used here (from werkzeug.utils import secure_filename)
            image_url = url_for('uploaded_file', filename=filename)
            # Here you would normally process the image and question with your model
            prediction = "Dummy prediction result"  # Replace with actual prediction logic
            return render_template('result.html', image_url=image_url, question=question, prediction=prediction)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0',port=5001