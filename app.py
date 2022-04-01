# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:41:19 2022

@author: User
"""


from flask import Flask
app=Flask(__name__)
from flask import request,render_template
import joblib

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        description=request.form.get("description")
        model=joblib.load("Q1")
        pred=model.predict(description)
        print(pred)
        pred=pred[0]
        s="The predicted theme is " + str(pred)
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="Predict 2"))
    
if __name__=="__main__":
    app.run()
    
    

