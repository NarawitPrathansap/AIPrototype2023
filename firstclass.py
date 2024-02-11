from email import message
from flask import Flask, request, render_template, make_response,url_for
import sys
import json
import os

app = Flask(__name__)


# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#api
@app.route('/request',methods=['POST'])
def web_service_API():
    
    payload = request.data.decode('utf-8')
    inmessage = json.loads(payload)

    print(message)

    json_data = json.dumps({'y':'recieved'})
    return json_data 
    
@app.route("/")  
def helloworld():
    return "Hello, World!"

@app.route("/name")  
def hellofirst():
    return "Hello, First!"

@app.route("/home",methods=['POST','GET'])  
def homefn():
    if request.method == "GET":

        print('we are in home(GET)',file=sys.stdout)
        namein = request.args.get("fname")
        print(namein, file=sys.stdout)
        return render_template("home.html",name=namein)

    elif request.method == "POST":
        print('we are in home(POST)',file=sys.stdout)
        namein = request.form.get("fname")
        lastnamein = request.form.get("lname")
        print(namein, file=sys.stdout)
        print(lastnamein,file=sys.stdout)
        return render_template("home.html",name=namein)
    
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']     
        file.save('filename')
        return render_template("home.html",name='upload complete')

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/webapp',methods=['GET','POST'])
def deeptooth_webapp():
    if request.method == 'POST':
        return render_template('web.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0',port=5001