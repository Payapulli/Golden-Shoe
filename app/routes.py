import os
import secrets
import base64
from flask import Flask, render_template, url_for, flash, redirect, request, session, g
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime, timedelta
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, SearchForm, UpdateAccountForm, OrderForm
from app.models import User, Product, Cart


@app.before_request
def before_request():
    g.search_form = SearchForm()

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/men")
def men():
    return render_template('men.html')

@app.route("/women")
def women():
    return render_template('women.html')

@app.route("/size_guide")
def size_guide():
    return render_template('size_guide.html')

@app.route('/search', methods=['POST'])
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('home'))
    return redirect(url_for('search_results', query=g.search_form.search.data))

@app.route('/search_results/<query>')
def search_results(query):
    qstring = "%{}%".format(query)
    prod = Product.query.filter(Product.name.like(qstring)).all()
    length = len(prod)
    img=[]
    for p in prod:
        img.append(base64.b64encode(p.image_file1).decode('ascii'))
    return render_template('search_results.html', title='Search Results', query=query, prod=prod, length=length, img=img)

@app.route("/signup", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Successfully created your account', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            if 'url' in session and session['url'] != None:
                return redirect(session['url'])
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email

    return render_template('account.html', title='Account', form=form)

@app.route("/product<int:id>", methods=['GET', 'POST'])
def product(id):
    session['url'] = None
    sizes = []
    prod = Product.query.filter_by(pid=id).first_or_404("This product does not exist")
    
    # Get sizes attached to this product_type_id
    products = Product.query.filter_by(product_type_id=prod.product_type_id).all()
    for i in products:
        sizes.append(i.size)

    img=[]
    img.append(base64.b64encode(prod.image_file1).decode('ascii'))
    if prod.image_file2:
        img.append(base64.b64encode(prod.image_file2).decode('ascii'))
    if prod.image_file3:
        img.append(base64.b64encode(prod.image_file3).decode('ascii'))
    if prod.image_file4:
        img.append(base64.b64encode(prod.image_file4).decode('ascii'))
    form = OrderForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            session['url'] = url_for('product', id=id)
            flash('You must log in first', 'danger')  
            return redirect(url_for('login'))
        
        found = False
        for product in products:
            if product.size == int(form.size.data):
                found = True
                selected_product = product
        
        if found == False:
            flash('This size is not available', 'danger') 
            return redirect(url_for('product', id=id))
        
        if form.quantity.data <= 0:
            flash('Invalid quantity', 'danger')
        elif (form.quantity.data > selected_product.stock):
            s='Requested quantity exceeds stock, only {stock} pieces available'.format(stock=selected_product.stock)
            flash(s, 'danger')
        else:
            cart = Cart.query.filter_by(pid=selected_product.pid).first()
            if cart != None:
                cart.quantity += form.quantity.data
                db.session.commit()
            else:
                new_cart = Cart(uid=current_user.id, pid=selected_product.pid, quantity=form.quantity.data)
                db.session.add(new_cart)
                db.session.commit()
            flash('The product was added to your cart!', 'success')

    return render_template('product_page.html', title='Product Details', prod=prod, img=img, form=form, sizes=sizes)

@app.route("/cart")
@login_required
def cart():
    cart = Cart.query.filter_by(uid=current_user.id).all()
    product_names = []
    product_sizes = []
    cost=[]
    for i in range(len(cart)):
        product = Product.query.filter_by(pid=cart[i].pid).first()
        
        if(product.stock < cart[i].quantity):
            s='Removing Item: {item}. Requested quantity exceeds stock, only {stock} pieces available'.format(item=product.name, stock=product.stock)
            flash(s, 'danger')
            Cart.query.filter_by(uid=current_user.id, pid=product.pid).delete()
            db.session.commit()
        else:
            product_names.append(product.name)
            product_sizes.append(product.size)
            cost.append(round(product.cost * cart[i].quantity, 2))
    
    # Update cart after potentially deleting item due to order being too large
    cart = Cart.query.filter_by(uid=current_user.id).all()
    total = round(sum(cost), 2)
    return render_template('cart.html', title='Cart', product_names=product_names, product_sizes=product_sizes, cost=cost, cart=cart, total=total, l=len(cart))

@app.route("/removeitem<int:id>")
@login_required
def removeitem(id):
    cart = Cart.query.filter_by(uid=current_user.id).all()
    if len(cart) == 0:
        flash('No item to remove from cart', 'warning')
        return redirect(url_for('home'))
    else:
        found = False
        for i in range(len(cart)):
            if id == cart[i].pid:
                found = True
                Cart.query.filter_by(uid=current_user.id, pid=id).delete()
                db.session.commit()
                flash('Item removed', 'success')
                break
        if found == False:
            flash('Item not present in cart', 'warning')
    product_names = []
    product_sizes = []
    cost = []
    cart = Cart.query.filter_by(uid=current_user.id).all()
    for i in range(len(cart)):
        product = Product.query.filter_by(pid=cart[i].pid).first()
        product_names.append(product.name)
        product_sizes.append(product.size)
        cost.append(round(product.cost * cart[i].quantity, 2))
    total = sum(cost)
    return render_template('cart.html', title='Cart', product_names=product_names, product_sizes=product_sizes, cost=cost, cart=cart, total=total, l=len(cart))

@app.route("/checkout", methods=['GET', 'POST'])
@login_required 
def checkout():
    cart = Cart.query.filter_by(uid=current_user.id).all()
    if len(cart) == 0:
        flash('There is nothing in your cart', 'warning')
        return redirect(url_for('home'))
    else:
        user = User.query.filter_by(id=current_user.id).first()
        flash('Order placed successfully', 'success')
        for i in range(len(cart)):
            # Update stock
            product = Product.query.filter_by(pid=cart[i].pid).first()
            product.stock -= cart[i].quantity
            db.session.commit()
        # Clear cart
        Cart.query.filter_by(uid=current_user.id).delete()
        db.session.commit()

        return render_template('checkout.html', title='Checkout')