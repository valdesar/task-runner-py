from flask import Flask, redirect, url_for, request
from flask import render_template
#, flash, redirect, render_template, request, session, abort
app = Flask(__name__)


@app.route('/')
def hell(name=None):
#    return "<h1>Hello World!</h1>"
#    return render_template('hello.html', name="new user")
#    return "List of task"
     with open("test.txt","r") as fo:
        res = fo.read()
#         fo.flush()
     return "Here tasks go: " + res



@app.route('/form')
def form(name=None):
#    return "<h1>Hello World!</h1>"
    return render_template('form.html')


#@app.route('/<name>')
#def hello_name(name):
#    return "Hello {}!".format(name)

#@app.route("/hello/<string:name>/")
#def hello(name):
#    return render_template(
#        'test.html',name=name)


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



@app.route('/new',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST': 
      user = request.form['nm'] 
      with open("test.txt","a") as fo:
         fo.write(user)
         fo.flush()
      return redirect(url_for('success',name = user)) 
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 



@app.route('/success/<name>') 
def success(name): 
   return 'welcome %s' % name 

#@app.route('/user/<username>')
#def show_user_profile(username):
    # show the user profile for that user
#    return 'User %s' % username


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="81")