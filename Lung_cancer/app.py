import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection , metrics
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/', methods=['GET'])
def home1():
    return render_template('index.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
   model = pickle.load(open('model2.pkl','rb'))
   gender = request.form.get('gender')
   if gender=="male":
      gender=1
   else:
      gender=0

   age = int(request.form.get('age'))

   smoking = request.form.get('smoking')
   if smoking=="yes":
      smoking=2
   else:
      smoking=1

   yellowfingers = request.form.get('yellowfingers')
   if yellowfingers=="yes":
      yellowfingers=2
   else:
      yellowfingers=1

   anxiety = request.form.get('anxiety')
   if anxiety=="yes":
      anxiety=2
   else:
      anxiety=1

   peerpressure = request.form.get('peerpressure')
   if peerpressure=="yes":
      peerpressure=2
   else:
      peerpressure=1

   chronicdisease = request.form.get('chronicdisease')
   if chronicdisease=="yes":
      chronicdisease=2
   else:
      chronicdisease=1

   fatigue = request.form.get('fatigue')
   if fatigue=="yes":
      fatigue=2
   else:
      fatigue=1

   allergy = request.form.get('allergy')
   if allergy=="yes":
      allergy=2
   else:
      allergy=1

   wheezing = request.form.get('wheezing')
   if wheezing=="yes":
      wheezing=2
   else:
      wheezing=1

   alcohol = request.form.get('alcohol')
   if alcohol=="yes":
      alcohol=2
   else:
      alcohol=1

   coughing = request.form.get('coughing')
   if coughing=="yes":
      coughing=2
   else:
      coughing=1

   breath = request.form.get('breath')
   if breath=="yes":
      breath=2
   else:
      breath=1

   swallowingDifficulty = request.form.get('swallowingDifficulty')
   if swallowingDifficulty=="yes":
      swallowingDifficulty=2
   else:
      swallowingDifficulty=1

   chestpain = request.form.get('chestpain')
   if chestpain=="yes":
      chestpain=2
   else:
      chestpain=1
      
   X_TEST=[[gender,age,smoking,yellowfingers,anxiety,peerpressure,chronicdisease,fatigue,allergy,wheezing,alcohol,coughing,breath,swallowingDifficulty,chestpain]]

   prediction = model.predict(X_TEST)
   print(prediction)
   
   if(prediction[0]=="YES"):
      prediction=0
   else:
      prediction=1
    
   return render_template('result.html',prediction=prediction)
   
if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=True)