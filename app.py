from flask import Flask, render_template, request, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
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
            
            # Load the image
            img = Image.open(image_path)
            width, height = img.size
            frac = 0.6

            # Correct the crop method call, should use a tuple for the box
            # Crop 60% from the left of the image
            crop_left_width = int(width * frac)
            cropped_left = img.crop((0, 0, crop_left_width, height))
            left_filename = 'left_' + filename
            left_image_path = os.path.join(app.config['UPLOAD_FOLDER'], left_filename)
            cropped_left.save(left_image_path)

            # Crop 60% from the right of the image and flip it
            crop_right_width = width - crop_left_width
            cropped_right = img.crop((crop_right_width, 0, width, height))
            flipped_right_side = cropped_right.transpose(Image.FLIP_LEFT_RIGHT)
            right_filename = 'right_' + filename
            right_image_path = os.path.join(app.config['UPLOAD_FOLDER'], right_filename)
            flipped_right_side.save(right_image_path)

            # Generate URLs for the images
            left_image_url = url_for('uploaded_file', filename=left_filename)
            right_image_url = url_for('uploaded_file', filename=right_filename)

            # Print the received question for debugging
            print("Received question:", question)
            prediction = "Dummy prediction result"  # Replace with your model's prediction logic

            # Render the result template with the image URLs
            return render_template('result.html', 
                                   cropped_image_url=left_image_url,
                                   flipped_image_url=right_image_url,
                                   question=question, 
                                   prediction=prediction)
        else:
            print('File type not allowed')
            return redirect(request.url)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0',port=5001