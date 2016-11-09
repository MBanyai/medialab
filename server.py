from flask import *
import os
import cv2
import base64
import numpy

app = Flask(__name__, template_folder ='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():

    temp=bytearray(base64.b64decode(request.data))
    file=open("static/temp.jpg",'wb')
    file.write(temp)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

