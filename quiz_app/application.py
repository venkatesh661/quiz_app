from flask import Flask, render_template, jsonify, request,redirect,flash,session
from models import *
import random
folder_name="static"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:********@127.0.0.1:3306/quiz"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = b'hkahs3720/' # use a random string
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
db.init_app(app)

#to change color of question buttons and disable 
def setStatus(qlist):
    qAttempt=[]
    strval=session['result'].strip()
    ans=strval.split(',')
    for i in range(int(len(ans)/2)):
        qAttempt.append(int(ans[2*i]))  
    
    for rw in qlist:
        if rw.qid in qAttempt:
            rw.bcol='green'   # set color
            rw.status='disabled' # disable

@app.route("/")
def index():
    session['result']=""
    subList=questions.query.with_entities(questions.subject).distinct()
    return render_template("index.html",subList=subList)

@app.route('/quiz', methods=["POST"])
def quiz(): 
    subject= request.form.get('sub')
    questList=questions.query.filter_by(subject=subject).all()
    quest=questions.query.filter_by(subject=subject).first()
    return render_template("dashboard.html",questList=questList, quest=quest) 

@app.route('/add', methods=["POST"])
def add():
    subject= request.form.get('sub')
    questList=questions.query.filter_by(subject=subject).all()
    quest=questions.query.filter_by(subject=subject).first()
    return render_template("add.html",questList=questList, quest=quest) 
    
@app.route('/addnewquestion', methods=["GET","POST"])
def addnewquestion():
    if request.method == 'POST':
        content = request.form.to_dict()
        output = questions.insert_data(content)
        return render_template("add.html")
    else:
        print('in else')
    return render_template("add.html")


@app.route('/delete', methods=["POST"])
def delete():
    questList=questions.query.all()
    print(questList)
    return render_template("delete.html", questList=questList) 
    
@app.route('/deletequestion', methods=["GET","POST"])
def deletequestion(): 
    if request.method == 'POST':
        content = request.form.to_dict()
        qids_to_delete = list(content.keys())
        questions.delete_data(qids_to_delete)
        questList=questions.query.all()
        print(questList)
        return render_template("delete.html", questList=questList)
    else:
        print('in else')
    return render_template("delete.html")


@app.route('/edit', methods=["POST"])
def edit():
    questList=questions.query.all()
    print(questList)
    return render_template("edit.html", questList=questList)


@app.route('/modification', methods=["POST"])
def modification():
    subject= request.form.get('sub')
    if request.method == 'POST':
        content = request.form.to_dict()
        qids_to_edit = list(content.keys())
        quest=questions.query.filter_by(qid=qids_to_edit).first()
        print(f'quest is {quest}')
        return render_template("update.html", quest=quest)
    else:
        return 'Check with Team'


@app.route('/update', methods=["POST"])
def update():
    subject= request.form.get('sub')
    questList=questions.query.all()
    quest=questions.query.filter_by(subject=subject).first()
    content = request.form.to_dict()
    print(f'content is {content}')
    output = questions.update_data(content)
    return render_template("edit.html",questList=questList, quest=quest)


@app.route("/showQuest/<string:subject>,<int:qid>")
def showQuest(subject,qid):
    questList=questions.query.filter_by(subject=subject).all()
    quest=questions.query.filter_by(qid=qid).first()
    setStatus(questList)
    return render_template("dashboard.html",questList=questList, quest=quest)  
    
@app.route('/saveAns',methods=["POST"]) 
def saveAns():
    qid=request.form.get('qid')
    ans=request.form.get('answer')
    sub=request.form.get('subject')
    #update the question id and its selected answer in session variable result
    res=session['result']
    print(f'res is {res}, qid is {qid}, ans is {ans}')
    res= res+qid+','+ans+','
    session['result']=res
    questList=questions.query.filter_by(subject=sub).all()
    setStatus(questList)
    quest=questions.query.filter_by(qid=qid).first()
    return render_template("dashboard.html",questList=questList, quest=quest)  
        
@app.route("/logout")
def logout():
    #calculate result
    count=0
    txt=""
    strval=session['result'].strip()
    #split result string by ','
    ans=strval.split(',')
    for i in range(int(len(ans)/2)):
        qd=ans[2*i] # get question id
        qn=ans[2*i+1]  # get the sorresponding answer
        tt=int(qd)
        quest=questions.query.filter_by(qid=tt).first()
        actans=quest.answer
        if actans==int(qn):#compare correct answer in questions table with answer chosen by user
            count=count+1 # increment counter
    txt=txt+'You have '+ str(count)+ ' correct questions out of '+ str(int(len(ans)/2))+ ' questions ' # set the result statement
    return render_template("result.html",txt=txt) 

# This is a comment line.we can use comments 
# Below is the line for main function.
# we are writing the code to push changes in the remote repository.


# main driver function sd our first branch
if __name__ == '__main__':
	app.run()