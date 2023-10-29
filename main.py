from flask import Flask, render_template, request, flash, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from web3 import Web3, HTTPProvider
import utility as u
app = Flask(__name__)
app.secret_key = 'your_secret_key'



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        role=request.form['role']
        if(u.checkuser(email, password, role)):
            flash('successfully logined','success')
            print(email, password, role)
            if(role=='Manufacturer'):
                return redirect(url_for('manufacturer'))
            elif(role=='Customer'):
                return redirect(url_for('customer'))
            elif(role=='Distributor'):
                return redirect(url_for('distributor'))
            elif(role=='ownsellers'):
                return redirect(url_for('retailer'))
        else:
            flash('Invalid Credentials','danger')
            return redirect(url_for('login'))
        
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        role=request.form['role']
        if(u.createuser(email, password, role)):
            flash('successfully registered','success')
            return redirect(url_for('login'))
        else:
            flash('Invalid Credentials','danger')
            return redirect(url_for('register'))
    
    return render_template('signup.html')  
        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Manufacturer')
def manufacturer():
    return render_template('manufacturer.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/distributor')
def distributor():
    return render_template('distributor.html')

@app.route('/retailer')
def retailer():
    return render_template('retailer.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/Manufacturer/addproduct', methods=['GET', 'POST'])
def addproduct():
    if session['role'] == 'Manufacturer' and session['logged_in'] == True:
        if request.method == 'POST':
            product_name=request.form['ProductName']
            product_id=request.form['product_id']
            status=request.form['status']
            destination=request.form['destination']
            remarks=request.form['remarks']
            role='Manufacturer'
            source='Factory Main Line'
            if(u.addProductToBlock(product_name, product_id, status, source, destination, remarks, role)):
                flash('successfully added','success')
                return redirect(url_for('manufacturer'))
            else:
                flash('Block Not Added to Blockchain','danger')
                return redirect(url_for('addproduct'))
        return render_template('addproduct.html')
    else:
        return redirect(url_for('login'))
        
        
        
        

@app.route('/manufacturer/viewproduct')
    

app.run(debug=True)