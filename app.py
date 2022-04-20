from flask import Flask,render_template,request
import random as r

app=Flask(__name__,static_url_path='/static')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/nam",methods=['POST','GET'])
def nam():
    if request.method=='POST':
        s,a,b=request.form['s1'],request.form['a1'],request.form['b1']
        s,a,b=int(s),int(a),int(b)
        st=''
        for i in range(s):
            st+=' '+str(r.randint(a,b))
        return render_template("nam.html", item=st)
   
app.run(port=5000)