from flask import Flask,render_template,request
import numpy as np
import joblib
app=Flask(__name__)


@app.route('/predict',methods=['GET','POST'])
def predict():
    
    if request.method=='POST':
        
        testdata=[ float(item) for item in request.form.values() ]
        
        print(f"Test data = {testdata}")         
        
        model=joblib.load('./knncrop.pkl')
        
        pred=model.predict(np.array([testdata]))
        
        print(f"Result of prediction = {pred}")
        
        result=pred[0]
        
        print(f"result = {result} , its type = {type(result)}")
        if result == 1:
            msg = "Predicted crop is rice"
        elif result == 2:
             msg = "Predicted crop is maize"
        elif result == 3:
             msg = "Predicted crop is chickpea"
        elif result == 4:
            msg = "Predicted crop is kidneybeans"
        elif result == 5:
             msg = "Predicted crop is pigeonbeans"
        elif result == 6:
            msg = "Predicted crop is mothbeans"
        elif result == 7:
            msg = "Predicted crop is mungbeans"
        elif result == 8:
            msg = "Predicted crop is blackgram"
        elif result == 9:
            msg = "Predicted crop is lentil"
        elif result == 10:
            msg = "Predicted crop is pomegranate"
        elif result == 11:
            msg = "Predicted crop is banana"
        elif result == 12:
            msg = "Predicted crop is mango"
        elif result == 13:
            msg = "Predicted crop is grapes"
        elif result == 14:
            msg = "Predicted crop is watermelon"
        elif result == 15:
            msg = "Predicted crop is muskmelon"
        elif result == 16:
            msg = "Predicted crop is apple"
        elif result == 17:
            msg = "Predicted crop is orange"
        elif result == 18:
            msg = "Predicted crop is papaya"
        elif result == 19:
            msg = "Predicted crop is coconut"
        elif result == 20:
            msg = "Predicted crop is cotton"
        elif result == 21:
            msg = "Predicted crop is jute"
        elif result == 22:
            msg = "Predicted crop is coffee"
        return render_template('homepage.html',result=msg)

@app.route('/login',methods=['GET','POST'])
def login():
    
    if request.method=='POST':
        
        uname=request.form['uname']
        pwd=request.form['pwd']
        
        if uname=="anu" and pwd=="anu@123":
            return render_template('homepage.html')
        else:
            return render_template('login.html',result="Login failed")

@app.route('/')
def index():
    return render_template('login.html')


if __name__=='__main__':
    
    app.run(debug=True)