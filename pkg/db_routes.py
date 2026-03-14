from flask import render_template,redirect
from sqlalchemy import desc,and_,or_
from sqlalchemy.sql import text
from pkg import app
from pkg.models import db,user,Participant,Customer,Category,Product,Brand


@app.route('/insertuser/')
def insert_user():
    query = "INSERT INTO user(name,email,message) VALUES('Mark Zeck','mz@gmai.com','Hi')"
    result = db.session.execute(text(query))
    db.session.commit()
    return f"User with id:{result.lastrowid} was inserted successfully!"


@app.route('/fetchusers/')
def fetchusers():
    query = "SELECT * FROM user"
    records = db.session.execute(text(query)) 
    r = records.fetchall()
    # print(r)
    # return f'Records fetched: {r}'
    return render_template('user.html',records=r)

@app.route('/deleteuser/<int:user_id>/')
def deleteuser(user_id):
    query = f"DELETE FROM user WHERE id={user_id}"
    db.session.execute(text(query))
    db.session.commit()
    return redirect('/fetchusers/')


@app.route('/insertuser2/')
def insert_user2():
    result = user.insert().values(name='Elon Musk',email='em@spacex.com',message='I love tech')
    db.session.execute(result)
    db.session.commit()
    return redirect('/fetchusers/')


@app.route('/updateuser/')
def updateuser():
    name = 'Mark Zeuk'
    message = 'I created facebook'
    result = db.update(user).where(user.c.id==2).values(name=name,message=message)
    db.session.execute(result)
    db.session.commit()
    return redirect('/fetchusers/')


@app.route('/participant/insert/')
def participant_insert():
    query = db.insert(Participant).values(username='sallydoe')
    db.session.execute(query)
    db.session.commit()
    return 'Participant saved successfully!'


@app.route('/participant/update/')
def participant_update():
    query = db.update(Participant).where(Participant.id==1).values(username='markhenry')
    db.session.execute(query)
    db.session.commit()
    return 'Participant updated successfully!'


@app.route('/orm/insert/')
def orm_insert():
    # c = Customer(cust_name='Bola Ahmed',cust_email='ba@company.org',cust_phone='08067373739')
    # db.session.add(c)
    # db.session.commit()
    # return f'Customer saved successfully with ID:{c.cust_id}!'

    c1 = Customer(cust_name='Peter Obi',cust_email='po@company.org',cust_phone='07073737283')
    c2 = Customer(cust_name='Atiku Abuba',cust_email='aa@company.org',cust_phone='0209383833')
    c3 = Customer(cust_name='Aliko Dangote',cust_email='ad@company.org',cust_phone='06074637383')
    db.session.add_all([c1,c2,c3])
    db.session.commit()
    return f'Customers saved successfully with IDs: {c1.cust_id} | {c2.cust_id} | {c3.cust_id}!'


@app.route('/orm/fetch/')
def orm_fetch():
    # customers = db.session.query(Customer.cust_id,Customer.cust_name).all()
    # customers = db.session.query(Customer).order_by(Customer.cust_name).all()
    # customers = db.session.query(Customer).order_by(desc(Customer.cust_name)).all()
    # customers = db.session.query(Customer).order_by(Customer.cust_name.desc()).all()
    # customers = db.session.query(Customer).offset(2).all()
    # customers = db.session.query(Customer).limit(2).all()
    # customers = db.session.query(Customer.cust_name,Customer.cust_email).all()
    # print(db.session.query(Customer.cust_name,Customer.cust_email))
    # print(customers)
    # customers = Customer.query.all()
    # print(type(customers))
    # return f'{customers}'
    total_customers = db.session.query(Customer).count()
    # cust = db.session.query(Customer).first()
    # cust = db.session.query(Customer).first_or_404()
    # print(cust)
    # cust = db.session.query(Customer).get('abc')
    # print(cust)

    # Working with the filter() method in orm
    # customers = db.session.query(Customer).filter(Customer.cust_id==5).all()
     # print(customers)
    # customers = db.session.query(Customer).filter(Customer.cust_id>=3,Customer.cust_id<=5).all()
    # customers = db.session.query(Customer).filter(Customer.cust_name=='Frank Mba',Customer.cust_email=='fm@company.org').all()
    # customers = db.session.query(Customer)\
    # .filter(and_(Customer.cust_name=='Peter Obi',Customer.cust_email=='po@company.org')).all()
    # customers = db.session.query(Customer)\
    # .filter(db.and_((Customer.cust_name=='Peter Obi'),(Customer.cust_email=='po@company.org')))\
    # .all()
    # customers = db.session.query(Customer)\
    # .filter((Customer.cust_name=='Bola Ahmed')|(Customer.cust_name=='Aliko Dangote'))\
    # .all()
    # customers = db.session.query(Customer)\
    # .filter(or_((Customer.cust_name=='Bola Ahmed'),(Customer.cust_name=='Aliko Dangote')))\
    # .all()
    # customers = db.session.query(Customer)\
    # .filter(db.or_((Customer.cust_name=='Bola Ahmed'),(Customer.cust_name=='Aliko Dangote')))\
    # .all()
    # customers = Customer.query.filter(Customer.cust_name != 'Peter Obi').all()
    # customers = Customer.query.filter(Customer.cust_name.ilike('%ik%')).all()
    # customers = Customer.query.filter(Customer.cust_id.in_([1,4])).all()
    # customers = Customer.query.filter(~Customer.cust_id.in_([1,4])).all()
    # customers = Customer.query.filter(Customer.cust_id.not_in([2,4])).all()
    # customers = Customer.query.filter(Customer.cust_phone == None).all()
    # customers = Customer.query.filter(Customer.cust_phone != None).all()
    # customers = db.session.query(Customer).filter_by(cust_phone='111111111111',cust_email='aa@sahara.com').all()
    customers = Customer.query.filter(Customer.cust_email.endswith('@company.org')).all()
    return render_template('orm_fetch.html',customers=customers,total=total_customers)


@app.route('/get/customer/<cust_id>/')
def get_customer(cust_id):
    # customer = db.session.query(Customer).get(cust_id)
    customer = db.session.query(Customer).get_or_404(cust_id)
    return render_template('customer_details.html',customer=customer)


@app.route('/update/')
def update():
    customer = db.session.query(Customer).get(4)
    customer.cust_name = 'Atiku Abubakar'
    customer.cust_email = 'aa@sahara.com'
    customer.cust_phone = '111111111111'
    db.session.commit()
    return redirect('/orm/fetch/')


@app.route('/delete/')
def delete():
    customer = db.session.query(Customer).get(2)
    db.session.delete(customer)
    db.session.commit()
    return redirect('/orm/fetch/')


@app.route('/save-data/')
def save_data():
    # cat1 = Category(name="Electronics")
    # cat2 = Category(name="Fashion")
    # cat3 = Category(name="Food")

    # db.session.add_all([cat1,cat2,cat3])
    # db.session.commit()

    # product1 = Product(name='LG Smart TV',price='1200',category=1)
    # product2 = Product(name='HP Laptop',price='800',category=1)

    # product3 = Product(name='Gucci Polo',price='1000',category=2)
    # product4 = Product(name='Zara Bag',price='400',category=2)

    # product5 = Product(name='Dominos Pizza',price='500',category=3)
    # product6 = Product(name='KFC Chicken',price='600',category=3)

    # db.session.add_all([product1,product2,product3,product4,product5,product6])
    # db.session.commit()

    # brand1 = Brand(name='LG')
    # brand2 = Brand(name='HP')
    # brand3 = Brand(name='Gucci')
    # brand4 = Brand(name='Zara')
    # brand5 = Brand(name='Dominos')
    # brand6 = Brand(name='KFC')

    # db.session.add_all([brand1,brand2,brand3,brand4,brand5,brand6])
    # db.session.commit()

    product = db.session.query(Product).get(6)
    product.brand = 6
    db.session.commit()

    return 'Data saved!'


@app.route('/related-data/')
def related_data():
    # products = db.session.query(Product,Category).join(Category).all()
    # products = db.session.query(Product.name,Category.name).join(Category).all()
    # products = db.session.query(Product,Category)\
    # .outerjoin(Category,Product.category==Category.id)\
    # .all()
    # print(products[2][0].price)
    # print(products[0][1])
    # products = Product.query\
    # .join(Category).add_columns(Category.name,Category.id)\
    # .filter(Category.name=='Fashion').all()

    # products = Product.query\
    # .join(Category).join(Brand).add_columns(Category,Brand)\
    # .all()
    # return f'{products}'

    # products = Product.query\
    # .join(Category).join(Brand).add_columns(Category,Brand)\
    # .filter(Category.name=='Electronics').all()
    # return f'{products}'

    # product = Product.query.get(1)
    category = Category.query.get(3)

    return f'{category.products}'





































