from test_flask_ml import app
from flask import jsonify,Response
from test_flask_ml.models.classification_model import classification_model

@app.route("/status",methods=["GET"])
def status():
    return Response("Classification model API started",200)

@app.route("/predict",methods=["POST"])
def predict():
    cm = classification_model()
    resp = jsonify(cm.predict())
    resp.status_code = 200
    return resp
