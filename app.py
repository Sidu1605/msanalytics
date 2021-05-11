from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re

from flask import *
from flask import Flask, redirect, url_for, request, render_template

import requests
import pandas as pd
import numpy as np
import pickle



app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'



@app.route('/')
def home():
    return render_template('home.html')


model1 = pickle.load(open('models/vehicleperformancemodel.pkl', 'rb'))
@app.route('/vehicleperformance' , methods=['GET','POST'])
def vehicleperformance():
    if request.method == "POST":

        # Name
        name = request.form['name']
        if (name == 'others'):
            name_others = 1
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0
        
        elif (name == 'ford'):
            name_others = 0
            name_ford = 1
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'chevrolet'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 1
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0
        
        elif (name == 'plymouth'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 1
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'dodge'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 1
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0
        
        elif (name == 'amc'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'toyota'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 1
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0
        
        elif (name == 'datsun'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 1
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'volkswagen'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 1
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'buick'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 1
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0
        
        elif (name == 'pontiac'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 1
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'honda'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 1
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'mazda'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 1
            name_mercury = 0
            name_oldsmobile=0
        
        elif (name == 'mercury'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 1
            name_oldsmobile=0

        else:
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=1
        
        # Origin

        origin = int(request.form['origin'])
        if (origin == 1):
            origin_2 = 0
            origin_3 = 0
        elif (origin == 2):
            origin_2 = 1
            origin_3 = 0
        else :
            origin_2 = 0
            origin_3 = 1

        # year
        year = int(request.form['year'])
        Vehicle_Age = 2021 - year

        # Displacement
        displacement = int(request.form['displacement'])

        # Weight
        weight = int(request.form['weight'])

        # Horsepower
        horsepower = int(request.form['horsepower'])

        # Acceleration
        acceleration = int(request.form['acceleration'])

        # Cylinders
        cylinders = int(request.form['cylinders'])
        if (cylinders == 3):
            cylinders_4 = 0
            cylinders_5 = 0
            cylinders_6 = 0
            cylinders_8 = 0
        
        elif (cylinders == 4):
            cylinders_4 = 1
            cylinders_5 = 0
            cylinders_6 = 0
            cylinders_8 = 0
        
        elif (cylinders == 5):
            cylinders_4 = 0
            cylinders_5 = 0
            cylinders_6 = 1
            cylinders_8 = 0
        
        elif (cylinders == 6):
            cylinders_4 = 0
            cylinders_5 = 0
            cylinders_6 = 1
            cylinders_8 = 0
        
        else:
            cylinders_4 = 0
            cylinders_5 = 0
            cylinders_6 = 0
            cylinders_8 = 1
        
        vpprediction = model1.predict([[displacement,horsepower, weight, acceleration,Vehicle_Age, origin_2, origin_3, cylinders_4, cylinders_5,
                             cylinders_6, cylinders_8, name_buick, name_chevrolet,
                             name_datsun, name_dodge, name_ford, name_honda, name_mazda,
                             name_mercury, name_oldsmobile, name_others, name_plymouth,
                             name_pontiac, name_toyota, name_volkswagen]])

        output=round(vpprediction[0],2)

        flash("The Mileage Of Your Car Is  {} Km/l".format(output), "success")
        return redirect(request.url)


    return render_template('vpform.html')

model2 = pickle.load(open('models/diabetespredictionmodel.pkl', 'rb'))
@app.route('/diabetesprediction' , methods=['GET','POST'])
def diabetesprediction():
    if request.method == "POST":
        Age = int(request.form['age'])
        Pregnancies = int(request.form['pregnancy'])
        Glucose = int(request.form['glucose'])
        BloodPressure = int(request.form['bloodpressure'])
        SkinThickness = int(request.form['skinthickness'])
        Insulin = int(request.form['insulin'])
        BMI = int(request.form['bmi'])
        DiabetesPedigreeFunction = float(request.form['dmf'])

        dpprediction = model2.predict([[Age, Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI,
                                   DiabetesPedigreeFunction]])

        if  dpprediction == 0:
            flash("Alert ! You Are Diagnosed With Diabetes !", "warning")
            return redirect(request.url)
        else:
            flash("Cool ! You Are Not Diagnosed With Diabetes !", "success")
            return redirect(request.url)
    
    return render_template('dpform.html')

model3 = pickle.load(open('models/spamdetectionmodel.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
@app.route('/spamdetection' , methods=['GET','POST'])
def spamdetection():
    if request.method == "POST":
        message = request.form['description']
        msg = vectorizer.transform([message])
        sdprediction = model3.predict(msg)
        prediction = sdprediction[0]

        if  prediction == 1:
            flash("Warning ! Your Mail is a Spam !", "warning")
            return redirect(request.url)
        else:
            flash("Cool ! Your Mail is Not a Spam ! ", "success")
            return redirect(request.url)
         
    return render_template('sdform.html')


model4 = pickle.load(open('models/genderclassificationmodel.pkl', 'rb'))
dictvectorizer = pickle.load(open('dictvectorizer.pkl', 'rb'))
def features(name):
    name = name
    return {
        'first-letter': name[0], # First letter
        'first2-letters': name[0:2], # First 2 letters
        'first3-letters': name[0:3], # First 3 letters
        'last-letter': name[-1:],
        'last2-letters': name[-2:],
        'last3-letters': name[-3:],
    }
# Vectorize the features function
#features = np.vectorize(features)
@app.route('/genderclassification' , methods=['GET','POST'])
def genderclassification():
    if request.method == "POST":
        name = request.form['name']
        print(name)
        nm = features(name)
        gcprediction = model4.predict(dictvectorizer.transform(nm))
        prediction = gcprediction[0]

        if  prediction == 1:
            flash("The Gender For The Given Name Is Male!")
            return redirect(request.url)
        else:
            flash("The Gender For The Given Name Is Female!")
            return redirect(request.url)


    return render_template('gcform.html')






if __name__ == "__main__":
    app.run(debug=True)




