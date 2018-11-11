from flask import Flask, redirect, url_for, request
from flask import render_template



#, flash, redirect, render_template, request, session, abort
app = Flask(__name__)
app.debug = True

@app.route('/')
def hell():

#    global res
#    global res1
#    global res2
#    global res3


#    return "<h1>Hello World!</h1>"
#    return render_template('hello.html', name="new user")
#    return "List of task"
     with open("test.txt","r") as fo:
        if len(fo.read().split('\n')) == 0:
            res = res1 = res2 = res3 = " "

        if len(fo.read().split('\n')) == 1:
            res = res1 = res2 = res3 = " "
#            return render_template('tasks.html', name = res, name1 = res1, name2 = res2, name3 = res3)
#            fo.seek(0)
        fo.seek(0)
        if len(fo.read().split('\n')) == 2:
            res = fo.read().split('\n')[0]
            fo.seek(0)
            res1 = fo.read().split('\n')[1]
            res2 = res3 = " "
#            return render_template('tasks.html', name = res, name1 = res1, name2 = res2, name3 = res3)

        fo.seek(0)
        if len(fo.read().split('\n')) == 3:
            res = fo.read().split('\n')[0]
            fo.seek(0)
            res1 = fo.read().split('\n')[1]
            fo.seek(0)
            res2 = fo.read().split('\n')[2]
            fo.seek(0)
            res3 = " "
#            return render_template('tasks.html', name = res, name1 = res1, name2 = res2, name3 = res3)

        fo.seek(0)
        if len(fo.read().split('\n')) == 4:
            res = fo.read().split('\n')[0]
            fo.seek(0)
            res1 = fo.read().split('\n')[1]
            fo.seek(0)
            res2 = fo.read().split('\n')[2]
            fo.seek(0)
            res3 = fo.read().split('\n')[3]
            fo.seek(0)
        return render_template('tasks.html', name = res, name1 = res1, name2 = res2, name3 = res3)
#        else:
#            return "fuck"
#        res4 = fo.read().split(' ')[4]

#         fo.flush()
#     return "Here tasks go: " + res
#     return render_template('tasks.html', name = res, name1 = res1, name2 = res2, name3 = res3)



@app.route('/form')
def form(name=None):
#    return "<h1>Hello World!</h1>"
    return render_template('form.html')


@app.route('/remove')
def removetask(name=None):
#    return "<h1>Hello World!</h1>"
    return render_template('remove.html')


#@app.route('/remove')
#def form(name=None):
#    return "<h1>Hello World!</h1>"
#    return render_template('remove.html')



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
         fo.write("\n")
         fo.write(user)
         fo.flush()
      return redirect(url_for('success',name = user)) 
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 

@app.route('/success/<name>') 
def success(name): 
   return 'welcome %s' % name 


@app.route('/removeit',methods = ['POST', 'GET']) 
def rem(): 
   if request.method == 'POST': 
      user = request.form['nm']
      user = int(user)
      with open("test.txt","r") as fo:
#         targ = fo.read().strip('\n')[user]
         data = fo.readlines()
         data[user] = ''
         fo.close()

      with open('test.txt', 'w') as fo:
         fo.writelines( data )



         #targ.write("")
        # fo.flush()
      return redirect(url_for('removed',name = user)) 
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('removed',name = user)) 



@app.route('/removed/<name>') 
def removed(name): 
   return 'welcome %s' % name 

#@app.route('/user/<username>')
#def show_user_profile(username):
    # show the user profile for that user
#    return 'User %s' % username


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="81")