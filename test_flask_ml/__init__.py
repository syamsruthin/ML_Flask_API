from flask import Flask,request

app = Flask(__name__)

#Loading all the endpoints written in endpoints dir
from test_flask_ml.endpoints.ml_endpoints import predict

def main():
    print("called")
    app.run(host="0.0.0.0",port=6060)
    print("Server started")