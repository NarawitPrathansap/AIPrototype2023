from flask import Flask, render_template, request
import os

app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# Make sure to create the directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        question = request.form['question']
        
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            # Here you would normally pass the image and question to your model for prediction
            # For demonstration, we'll just return the question and filename
            return render_template('result.html', question=question, filename=file.filename)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0',port=5001
