from flask import Flask , redirect, url_for, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/flask/<name>')
def show_user(name):
    return "hey dd %s"%name

@app.route('/admin')
def admin():
    return "hello admin"

# app.add_url_rule('/hello','byy',show_user)

@app.route('/name/<name>')
def show_name(name):
    print(type(name))
    if name == "admin":
        return redirect(url_for("admin"))
    elif name == 'user':
        return redirect(url_for("show_user",name=name))
    
    return "hello !!!! %s"%name

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == "POST":
        username = request.form['nm']
        print("Your name: %s"%username)
        return "success"
    elif request.method == "GET":
        user = request.args.get("nm")
        print("This is get method : ",user)
        return "get Success"
    

@app.route("/uploader",methods=["POST"])
def uploader():
    if request.method == "POST":
        file = request.files['file']
        df = pd.read_csv(file)
        print("---------------------")
        print(df.head())
        print("---------------------------------")
        print("Your file: ",file)
        print("saving file--------------")
        file.save("E:\\Ganesh_Pun\\Flask\\flask_01\\file")
        return {"status":"Successfully sent "}
    



















if __name__ == "__main__":
    app.run("0.0.0.0","5000",debug=True)