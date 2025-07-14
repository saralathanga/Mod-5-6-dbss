from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index copy.html"))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    q = float(request.form.get("q"))
    
    # return(render_template("prediction.html",r=(-50.6*q)+90.2))

    # load model
    model = joblib.load("dbs.jl")

    # make prediction
    pred = model.predict([[q]])

    return(render_template("prediction.html",r=pred))

if __name__ == "__main__":
    app.run()

