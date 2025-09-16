from datetime import datetime
from flask_login import UserMixin
from app import app, db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    contactno = db.Column(db.Numeric(10, 0), unique=True)
    address_line1 = db.Column(db.String(50))
    address_line2 = db.Column(db.String(50))
    address_line3 = db.Column(db.String(50))
    pincode = db.Column(db.Integer)
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"


class Product(db.Model):
    __tablename__ = "product"
    pid = db.Column(db.Integer, primary_key=True)
    product_type_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    details = db.Column(db.String(500), nullable=False)
    image_file1 = db.Column(db.LargeBinary, nullable=True)
    image_file2 = db.Column(db.LargeBinary, nullable=True)
    image_file3 = db.Column(db.LargeBinary, nullable=True)
    image_file4 = db.Column(db.LargeBinary, nullable=True)
    size = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', Size {self.size}, ${self.cost})"


class Cart(db.Model):
    __tablename__ = "cart"
    uid = db.Column(db.Integer, db.ForeignKey(User.__table__.c.id), primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey(Product.__table__.c.pid), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Cart(User {self.uid}, Product {self.pid}, Qty {self.quantity})"