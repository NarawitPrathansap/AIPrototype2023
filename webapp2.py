from flask import Flask, render_template, request, redirect, url_for
import os
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('testweb.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    if file:
        # Save the original image
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process the image: cut in half and flip the left side to the right
        processed_filename = 'processed_' + filename
        processed_filepath = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
        process_and_save_image(filepath, processed_filepath)
        
        return 'Image uploaded and processed successfully'

def process_and_save_image(original_filepath, processed_filepath):
    with Image.open(original_filepath) as img:
        # Calculate the dimensions to split the image in half
        width, height = img.size
        left_side = img.crop((0, 0, width // 2, height))
        
        # Flip the left side horizontally
        flipped_left_side = left_side.transpose(Image.FLIP_LEFT_RIGHT)
        
        # Create a new image with the same size as the original
        new_img = Image.new('RGB', (width, height))
        
        # Paste the flipped left side into both halves of the new image
        new_img.paste(flipped_left_side, (0, 0))
        new_img.paste(flipped_left_side, (width // 2, 0))
        
        # Save the processed image
        new_img.save(processed_filepath)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0',port=5001
