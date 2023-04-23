
import pickle
from flask import Flask,render_template,request

app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        nutrients = [float(request.form.get("nitrogen")), float(request.form.get("phosphorous")), float(request.form.get("potassium")), float(request.form.get("temperature")), float(request.form.get("humidity")), float(request.form.get("ph")), float(request.form.get("rainfall"))]
        crop = model.predict([nutrients])[0]   
        return render_template("index.html", prediction_text=f"The predicted crop is {crop}")
    except Exception as e:
        print(str(e))
        return render_template("index.html", prediction_text=f"Something went wrong!! Kindly Check Values")


    # try:
    # nutrients = [float(request.form.get("nitrogen")), float(request.form.get("phosphorous")), float(request.form.get("potassium")), float(request.form.get("temperature")), float(request.form.get("humidity")), float(request.form.get("ph")), float(request.form.get("rainfall"))]
    # crop = model.predict([nutrients])[0]   
    # return render_template("index.html", prediction_text=f"The predicted crop is {crop}")
    
    # except:
    #  nutrients = [float(request.form.get("nitrogen")), float(request.form.get("phosphorous")), float(request.form.get("potassium")), float(request.form.get("temperature")), float(request.form.get("humidity")), float(request.form.get("ph")), float(request.form.get("rainfall"))]
    # crop = model.predict([nutrients])[0]   
    # return render_template("index.html", prediction_text=f"Something Went wrong")



if __name__=="__main__":
    app.run(debug=True)
