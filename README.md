# Sample Quiz app 
 This  is a Quiz	web site, show random 10 quetion one by one and show result at end.	Ability to add/edit/delete questions	login functionality and stroring scores of users in quiz.
  ![Home Page](https://user-images.githubusercontent.com/120723992/211252662-06db8201-ff8d-4c02-9b57-cd412ce3ceda.jpeg)
 	 	Ability to create a quiz from added questions, in such a way that at one time one question is returned. When users clicks next, next question is returned. Condition question should not be repeated in same quiz.
    


![Quiz Page](https://user-images.githubusercontent.com/120723992/211255349-29a620e5-419c-446d-bd5a-4d3ca0bef27e.jpeg)


![Adding Question](https://user-images.githubusercontent.com/120723992/211255148-bc5c1507-049a-41ef-9e95-d77d90cff836.jpeg)

![Deleteing](https://user-images.githubusercontent.com/120723992/211255191-c086f85d-47df-4fc3-b78e-1dd015572fde.jpeg)


## Installation


For this project we need to install several python  modules like  Flask ,Sqlalchemy & mysql server

```bash
from flask import Flask, render_template, jsonify, request,redirect,flash,session
import random
from flask_sqlalchemy import SQLAlchemy![QuizPage](https://user-images.githubusercontent.com/120723992/211252452-0877bbc3-cc56-4df3-93cc-a0006b3fb876.jpeg)
```

## Usage

```python
from flask import Flask, render_template, jsonify, request,redirect,flash,session
from models import *
# returns 'no of subjects'
@app.route("/showQuest/<string:subject>,<int:qid>")
# returns 'Add'
@app.route('/addnewquestion', methods=["GET","POST"])
# returns 'Delete'
@app.route('/deletequestion', methods=["GET","POST"])
# returns 'Edit'
@app.route('/update', methods=["POST"])
# returns 'saving answer'
@app.route('/saveAns',methods=["POST"])
# returns 'Result'
@app.route('/logout',methods=["POST"])
```


Deployment
----------------
If you want to deploy this application in our local system we need to follow this below steps 

1. We need to install Mysql server, python and required modules.
2. Then need to pull the code and execute the sample sql file to create database and table.
