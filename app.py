from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    url_for,
    flash
    )
import pickle 
import numpy as np
import pandas as pd
from form import inputForm

model_path='model.pkl'

with open(model_path,'rb') as file:
    model=pickle.load(file)

app=Flask(__name__)
app.config["SECRET_KEY"]="007"

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',name="Home")

@app.route('/about')
def about():
    return render_template('about.html',name="About")

@app.route('/predict',methods=['GET','POST'])
def predict():
    form=inputForm()
    if request.method=='POST':
        planes=['SpiceJet' ,'AirAsia', 'Vistara' ,'GO_FIRST','Indigo' ,'Air_India']
        source= ['Delhi', 'Mumbai' ,'Bangalore' ,'Kolkata', 'Hyderabad', 'Chennai']
        departure_time=['Evening', 'Early_Morning', 'Morning' ,'Afternoon', 'Night' ,'Late_Night']
        stops=['zero' ,'one', 'two_or_more']
        arrival_time=['Night' ,'Morning', 'Early_Morning' ,'Afternoon' ,'Evening', 'Late_Night']
        destination_city=['Mumbai' ,'Bangalore', 'Kolkata' ,'Hyderabad' ,'Chennai' ,'Delhi']
        coach=['Economy','Business']
        input_1=planes.index(request.form.get('airline'))+1
        input_2=source.index(request.form.get('Source'))+1
        input_3=departure_time.index(request.form.get('departure'))+1
        input_4=stops.index(request.form.get('stops'))+1
        input_5=arrival_time.index(request.form.get('arrival'))+1
        input_6=destination_city.index(request.form.get('destination'))+1
        input_7=coach.index(request.form.get('coach'))+1
        input_8=float(request.form.get('duration'))
        input_9=int(request.form.get('daysLeft'))
        a=[input_1,input_2,input_3,input_4,input_5,input_6,input_7,input_8,input_9]

        feature_names = ['airline', 'source_city', 'departure_time', 'stops', 'arrival_time', 'destination_city', 'class', 'duration', 'days_left']
        input_data = pd.DataFrame([a], columns=feature_names)

        output=model.predict(input_data)
        out=float(output[0])
        out=round(out,2)
        output_str = str(out)
        flash(f'Estimated Price: {output_str}')
    return render_template('predict.html',name="Estimate Flight Prices",form=form)

if __name__=="__main__":
    app.run()