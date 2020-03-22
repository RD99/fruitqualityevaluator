from flask import Flask, send_from_directory, request,send_file
from flask_cors import CORS
import cv2
import numpy as np
import os
import base64
app = Flask(__name__, static_folder="../frontend/foe/build")
app.config['UPLOAD_FOLDER'] = '../../../backend'
CORS(app)


@app.route("/")
def hello():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:path>")
def static_proxy(path):
    """static folder serve"""
    file_name = path.split("/")[-1]
    dir_name = os.path.join(app.static_folder, "/".join(path.split("/")[:-1]))
    return send_from_directory(dir_name, file_name)


@app.route("/predict",  methods=['POST'])
def predict():
    filestr = request.files['file'].read()
    print(request.files['file'].filename)
    # convert string data to numpy array
    npimg = np.fromstring(filestr, np.uint8)
    # convert numpy array to image
    img = cv2.imdecode(npimg, cv2.COLOR_BGR2RGB)
    print(img.shape)
    cv2.imwrite("detect_fruits.jpg", img)
    print("Start")
    os.system("python procedure.py")
    with open('Final_Evaluation.jpg', "rb") as imageFile:
        img = base64.b64encode(imageFile.read())
    return img


if __name__ == '__main__':
    app.run()
