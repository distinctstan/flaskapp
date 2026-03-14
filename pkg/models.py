from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user = db.Table(
    'user',
    db.Column('id',db.Integer,primary_key=True),
    db.Column('name',db.String(200)),
    db.Column('email',db.String(100)),
    db.Column('message',db.String(100))
)

student = db.Table(
    'student',
    db.Column('id',db.Integer,primary_key=True),
    db.Column('name',db.String(200)),
    db.Column('reg_no',db.String(100))
)


class Participant(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(200),nullable=False)
    regdate = db.Column(db.DateTime,default=datetime.utcnow)


class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    fullname = db.Column(db.String(200),nullable=False)
    dept = db.Column(db.String(100))

    def __repr__(self):
        return self.fullname


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    content = db.Column(db.Text,nullable=False)
    created_on = db.Column(db.DateTime,default=datetime.utcnow)
    updated_on = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

    def __repr__(self):
        return f'{self.id}:{self.title[:10]}'


# cust_id, cust_name, cust_email, cust_phone, cust_datereg
class Customer(db.Model):
    cust_id = db.Column(db.Integer,primary_key=True)
    cust_name = db.Column(db.String(200),nullable=False)
    cust_email = db.Column(db.String(150),nullable=False,unique=True)
    cust_phone = db.Column(db.String(15))
    cust_datereg = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f'{self.cust_id}:{self.cust_name}'


class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    
    # Foreign Key Column linking to Category/Brand Model/Table
    category = db.Column(db.Integer,db.ForeignKey('category.id'))
    brand = db.Column(db.Integer,db.ForeignKey('brand.id'))

    # cat = db.relationship(Category, back_populates='products') 

    def __repr__(self):
        return f'<{self.id}:{self.name}>'
    

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)

    products = db.relationship(Product, backref='cat', lazy='dynamic')
    # products = db.relationship(Product, back_populates='cat')

    def __repr__(self):
        return f'<{self.id}:{self.name}>'


class Brand(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),nullable=False)

    products = db.relationship(Product, backref='bran')

    def __repr__(self):
        return f'<{self.id}:{self.name}>'


class State(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    lgas = db.relationship('Lga',backref="state")

class Lga(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    state_id = db.Column(db.Integer,db.ForeignKey('state.id'))

