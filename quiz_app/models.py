import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
   
class questions(db.Model):
    __tablename__="questions"
    qid = db.Column(db.Integer, primary_key=True)
    subject =db.Column(db.String, nullable=False)
    question =db.Column(db.String, nullable=False)
    option1 = db.Column(db.String, nullable=True)
    option2 = db.Column(db.String, nullable=True)
    option3 = db.Column(db.String, nullable=True)
    option4 = db.Column(db.String, nullable=True)
    answer = db.Column(db.Integer, nullable=True)
    bcol = db.Column(db.String, nullable=True)

    def insert_data(data):
        print(f'data is {data}')
        john = questions(**data)
        db.session.add(john)
        db.session.commit()

    def delete_data(data):
        print(f'data is ----{tuple(data)}')
        questions.query.filter(questions.qid.in_(tuple(data))).delete()
        db.session.commit()
    
    def update_data(data):
        print(f'data for update is {data}')
        inqid = data['qid']
        questions.query.filter_by(qid=inqid).update(data)
        db.session.commit()