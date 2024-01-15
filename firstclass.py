from flask import Flask, request, render_template, make_response 

import json

app = Flask(__name__)

@app.route("/")  
def helloworld():
    return "Hello, World!"

@app.route("/name")  
def hellowfirst():
    return "Hello, First!"

@app.route("/home2")  
def home2():
    return render_template("home.html",name='first')


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0',port=5001