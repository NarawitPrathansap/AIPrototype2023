from email import message
from flask import Flask, request, render_template, make_response
import sys
import json

app = Flask(__name__)

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
def hellowfirst():
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


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0',port=5001