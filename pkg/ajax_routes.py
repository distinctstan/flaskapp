import json
from flask import render_template,request,make_response,jsonify
from pkg import app
from pkg.models import Customer,Lga

@app.route('/ajax-load/')
def ajax_load():
    return render_template('ajax.html')


@app.route('/load-data/',methods=['GET','POST'])
def load_data():
    fn = request.form.get('firstname')
    age = request.form.get('age')
    return f"Data from the server: Firstname={fn} and Age={age}"

    # username = request.form.get('username')
    # email = request.form.get('email')
    # customer = Customer.query.filter(Customer.cust_email==email).first()
    # if customer:
    #     return f'A customer is already using this email: {email}'
    # else:
    #     return 'Everything looks good'


@app.route('/ajax/request/')
def ajax_request():
    return render_template('ajax_request.html')


@app.route('/ajax/response/',methods=['GET','POST'])
def ajax_response():
    # username = request.form.get('username')
    # password = request.form.get('password')
    # edu = request.form.get('edu')
    # photo = request.files.get('photo')
    # role = request.form.get('role')
    # if username == '':
    #     return 'Username field is required'
    # return f'Username:({username})|Password:({password})|Education:({edu})|Photo:({photo})|Role:({role})'

    username = request.form.get('username')
    password = request.form.get('password')
    jsondata = {'username':username,'password':password}
    # resp = make_response(json.dumps(jsondata),200)
    # resp.headers['Content-Type'] = 'application/json'
    # return resp
    # return jsonify(jsondata)
    return jsonify(username=username,password=password) # keyword args


@app.route('/search/')
def search_view():
    search = request.args.get('search')
    if search != '':
        customers = Customer.query.filter(Customer.cust_name.ilike(f'{search}%')).all()
    else:
        return ''
    results = '<p class="alert alert-warning">'
    if customers:
        for customer in customers:
            results += f'<span>{customer.cust_name}</span><br>'
    else:
        results += '<span>No customer found</span>'
    results += '</p>'
    return results


@app.route('/image/search/')
def search_image():
    images = '<p><img width="50%" src="/assets/images/pic1.jpg">' \
    '<img width="50%" src="/assets/images/pic2.jpg"></p>'
    return images


@app.route('/get/lgas/')
def get_lgas():
    state = request.args.get('state_id')
    lgas = Lga.query.filter(Lga.state_id==state).all()
    result = ''
    for lga in lgas:
        result += f'<option value="{lga.id}">{lga.name}</option>'
    return result
