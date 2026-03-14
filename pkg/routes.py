from flask import render_template,request,redirect,flash,make_response,session
from flask_mail import Message
from pkg import app,csrf,mail
from pkg.forms import UserDetail,SignUpForm

@app.after_request
def after_request(resp):
    resp.headers['Cache-Control'] = 'no-cache,no-store,must-revalidate'
    return resp

# @app.route('/',methods=['GET','POST'])
# def home():
#     if request.method == 'POST':
#         return 'Form has been submitted'
#     else:
#         return render_template('home.html')
    
@app.get('/')
def home_get():
    return render_template('home.html')

@app.post('/')
def home_post():
    # username = request.form['user']
    # password = request.form['pwd']
    # username = request.form.get('user','No username')
    # password = request.form.get('pwd','No password')
    # items = request.form.items()
    # print(dict(items))
    # with open('usersfile.txt','a') as f:
    #     f.write(f'========================\n')
    #     f.write(f'Username: {username}\n')
    #     f.write(f'Password: {password}\n')
    #     f.write(f'========================\n')
    #     f.write(f'\n\n')
    # return f'Form has been submitted'


    username = request.form.get('user','No username')
    password = request.form.get('pwd','No password')
    if username == '' or password == '':
        # flash('All fields are required')
        flash('All fields are required',category='error')
        return redirect('/')
    else:
        # flash('You are now registered')
        flash('You are now registered',category='success')
        return redirect('/notify/')


# @app.route('/register/',methods=['GET','POST'])
# def register():
#     # print(request.method)
#     if request.method == 'POST':
#         return "Form has been submitted"
#     else:
#         return 'Please submit the form'


@app.get('/login/')
def login():
    # username = request.args['user']
    # password = request.args['pwd']

    username = request.args.get('user')
    password = request.args.get('pwd')
    return f'Logged In with username:{username} - Password:{password}'


@app.get('/notify/')
def notify_get():
    return render_template('notify.html')

@app.post('/notify/')
def notify_post():
    email = request.form.get('email')
    contact = request.form.getlist('contact')

    # with open('subscribers.txt', 'a') as f:
    #     f.write(f'========================\n')
    #     f.write(email + '\n')
    #     f.write(f'========================\n\n')
    # return f'Your email: {email} has been saved successfully!'
    return f"""
        Email: {email}
        Contact: {contact}
    """

@app.get('/configitems/')
def configitems():
    items = app.config
    return render_template('configitems.html',items=items)


@app.get('/setcookie/')
def setcookie():
    resp = make_response('Your cookie has been set')
    resp.set_cookie('fullname','Frank Doe',max_age=3*24*60*60)
    return resp

@app.get('/getcookie/')
def getcookie():
    # request.cookies['fullname']
    fn = request.cookies.get('fullname')
    return f'This is your cookie: {fn}'


@app.route('/travel/',methods=['GET','POST'])
def travel():
    if request.method == 'POST':
        continent = request.form.get('continent')
        resp = make_response(redirect('/travel/'))
        resp.set_cookie('continent',continent,max_age=5*24*60*60)
        # resp.headers['Set-Cookie'] = 'continent='+continent
        return resp
    else:
        continent = request.cookies.get('continent')
        return render_template('travel.html',continent=continent)
    

@app.get('/deletecookie/')
def deletecookie():
    resp = make_response('Your cookie has been deleted or expired')
    resp.set_cookie('fullname',max_age=-3*24*60*60)
    return resp


@app.get('/setsession/')
def setsession():
    session['firstname'] = 'Mark'
    session['lastname'] = 'Zeuk'

    return 'Session data has been set'

@app.get('/getsession/')
def getsession():
    fname = session['firstname']
    lname = session.get('lastname') 

    return f'Firstname: {fname} || Lastname: {lname}'


@app.get('/signin/')
def signin():
    return render_template('login.html')

@app.post('/signin/')
@csrf.exempt
def signin_post():
    passcodes = ['1111','2222','3333','4444'] 
    username = request.form.get('username')
    password = request.form.get('password')
    if username != '' and password in passcodes:
        session['username'] = username
        return redirect('/dashboard/')
    else:
        return redirect('/signin/')

@app.get('/dashboard/')
def dashboard():
    if 'username' not in session:
        return redirect('/signin/') 
    return render_template('dashboard.html')

@app.get('/profile/')
def profile():
    # if 'username' not in session:
    #     return redirect('/signin/') 
    # return render_template('profile.html')
    if session.get('username') == None:
        return redirect('/signin/') 
    else:
        return render_template('profile.html')

@app.get('/logout/')
def logout():
    session.pop('username')
    return redirect('/signin/')


@app.route('/userdetails/',methods=['GET','POST'])
def userdetails():
    userform = UserDetail()
    if userform.validate_on_submit():
        return redirect('/')
    else:
        return render_template('userdetails.html',userform=userform)
    
@app.route('/signup/',methods=['GET','POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # username = request.form.get('username')
        # email = request.form.get('email')
        # password1 = request.form.get('password1')
        # password2 = request.form.get('password2')
        # return f'Username={username} and Email={email} and Password={password1}'
    
        username = form.username.data
        email = form.email.data
        password1 = form.password1.data
        password2 = form.password2.data
        return f'Username={username} and Email={email} and Password={password1}'
    return render_template('signup.html',form=form)


@app.route('/sendemail/')
def send_email():
    msg = Message(subject='Reminder',sender='demo@example.com',
                  recipients=['stanley@moatcohorts.com.ng'])
    # msg.body = 'We are learning how to send email from flask!'
    msg.html = """<div style="border:1px solid gray; padding:15px;">
                    <h1 style="background-color:red;color:yellow;padding:10px;">Payment Reminder</h1>
                    <p style="padding:5px;">Please endeavour to renew your subscription before next week!</p>
                </div>"""
    mail.send(msg)
    return 'Email has been sent!'


@app.route('/sendemail2/')
def send_email2():
    msg = Message(subject='Attaching a file',sender=('User','email@domain.com'),recipients=['stanley@moatcohorts.com.ng'])
    msg.html = """<div style="background-color:yellow;padding:10px;margin:0px 15px;">
                    <h1 style="background-color:blue;color:yellow;padding:10px;">Email Attachment</h1>
                    <p style="border:1px solid gray;padding:5px;">We are learning how to attach a file for email sending to our flask app!</p>
                    <button style="background-color:black;color:white;padding:5px 15px;">Get Started</button>
                </div>"""
    with app.open_resource('assets/images/pic1.jpg') as fd:
        msg.attach('pic1.jpg','image/jpg',fd.read())

    mail.send(msg)
    return 'Email sent with attachment!'