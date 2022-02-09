from flask import Flask, render_template, request
import sqlite3 as sql
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier


app = Flask(__name__)
# load the pickel model
model = pickle.load(open('Randomforest_rain_prediction.pkl','rb'))
# with open('Randomforest_rain_prediction.pkl') as mod:
#        model = pickle.load(mod)

@app.route('/')
def home():
   return render_template('page.html')



@app.route("/predict", methods = ['POST'])
def predict():
    features = []
    Location = request.form['Location']
    loc = {'Adelaide': 0, 'Albany': 1, 'Albury': 2, 'AliceSprings': 3, 'BadgerysCreek': 4, 'Ballarat': 5, 'Bendigo': 6, 'Brisbane': 7
    , 'Cairns': 8, 'Canberra': 9, 'Cobar': 10, 'CoffsHarbour': 11, 'Dartmoor': 12, 'Darwin': 13, 'GoldCoast': 14
    , 'Hobart': 15, 'Katherine': 16, 'Launceston': 17, 'Melbourne': 18, 'MelbourneAirport': 19, 'Mildura': 20, 'Moree': 21
    , 'MountGambier': 22, 'MountGinini': 23, 'Newcastle': 24, 'Nhil': 25, 'NorahHead': 26, 'NorfolkIsland': 27, 'Nuriootpa': 28
    , 'PearceRAAF': 29, 'Penrith': 30, 'Perth': 31, 'PerthAirport': 32, 'Portland': 33, 'Richmond': 34, 'Sale': 35, 'SalmonGums': 36
    , 'Sydney': 37, 'SydneyAirport': 38, 'Townsville': 39, 'Tuggeranong': 40, 'Uluru': 41, 'WaggaWagga': 42, 'Walpole': 43, 'Watsonia': 44
    , 'Williamtown': 45, 'Witchcliffe': 46, 'Wollongong': 47, 'Woomera': 48}
    Loca = loc[Location]
    features.append(Loca)

    MinTemp = request.form['MinTemp']
    
    
    if '.' in MinTemp :
        x = float(MinTemp)
        features.append(MinTemp)
    else:
        features.append(MinTemp)

    Rainfall = request.form['Rainfall']
    
    if '.' in Rainfall :
        x = float(Rainfall)
        features.append(Rainfall)
    else:
        features.append(Rainfall)
    WindGustSpeed = request.form['WindGustSpeed']
    
    if '.' in WindGustSpeed :
        x = float(WindGustSpeed)
        features.append(WindGustSpeed)
    else:
        features.append(WindGustSpeed)
    WindSpeed9am = request.form['WindSpeed9am']
    
    if '.' in WindSpeed9am :
        x = float(WindSpeed9am)
        features.append(WindSpeed9am)
    else:
        features.append(WindSpeed9am)
    WindSpeed3pm = request.form['WindSpeed3pm']
    
    if '.' in WindSpeed3pm :
        x = float(WindSpeed3pm)
        features.append(WindSpeed3pm)
    else:
        features.append(WindSpeed3pm)
    Humidity9am = request.form['Humidity9am']
    
    if '.' in Humidity9am :
        x = float(Humidity9am)
        features.append(Humidity9am)
    else:
        features.append(Humidity9am)
    Humidity3pm = request.form['Humidity3pm']
    
    if '.' in Humidity3pm :
        x = float(Humidity3pm)
        features.append(Humidity3pm)
    else:
        features.append(Humidity3pm)
    Pressure3pm = request.form['Pressure3pm']
    
    if '.' in Pressure3pm :
        x = float(Pressure3pm)
        features.append(Pressure3pm)
    else:
        features.append(Pressure3pm)
    RainToday = request.form['RainToday']
    if RainToday == 'Yes':
        features.append(1)
    else:
        features.append(0)
    category = ['E','ENE','ESE','N','NE','NNE','NNW','NW','S','SE','SSE','SSW','SW','W','WNW','WSW']
    cat1 = []
    WindGustDir = request.form['WindGustDir']
    for i in category:
        if i == WindGustDir:
            cat1.append(1)
        else:
            cat1.append(0)
    features = features + cat1
    cat2 = []
    WindDir3pm = request.form['WindDir3pm']
    for i in category:
        if i == WindDir3pm:
            cat2.append(1)
        else:
            cat2.append(0)
    features = features + cat2
    cat3 = []
    WindDir9am = request.form['WindDir9am']
    for i in category:
        if i == WindDir9am:
            cat3.append(1)
        else:
            cat3.append(0)
    features = features + cat3

    
    feature = [np.array(features)]
    
    
    prediction = model.predict(feature)

    if prediction == 1:
        prediction = 'Tomorrow is going to be rainy day  So enjoy yourselves with a cup of coffee and hot snack'
    else:
        prediction = 'Tomorrow is going to be sunny day  So enjoy yourselves with a cool milkshake and icecream'

    
    
    return render_template("page.html", prediction_text = "The predicted Rain is  :  {}".format(prediction))



if __name__ == '__main__':
    
     app.run(debug = True)
