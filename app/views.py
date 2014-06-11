from flask import Blueprint, render_template, g, redirect, request, url_for, flash, abort, session
from app.decorators import requires_login
from app.forms import LoginForm, RegistrationForm, DropoffForm, NewProductForm, ClientForm, FamilyForm
import base64
import sys
from readAtten import *
from writeAtten import writeAtten
from app.db import DBInterface
from app import app

mod = Blueprint('tools', __name__, url_prefix='/')

def connect_db():
    conn = DBInterface(app.config['DATABASE'])
    return conn

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.execute_script(f.read())

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@mod.route('/', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return render_template('index.html')
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        db = get_db()
        success = db.do_login(form.username.data, form.password.data)
        if success:
            session['logged_in'] = True
            session['user'] = form.username.data
            flash("You are logged in!")
            return render_template('index.html')
        else:
            print "Login failed"
            flash("Login information incorrect.")
    return render_template('login.html', form=form)

@mod.route('attenuator/', methods=['GET'])
def readValues():

    atten1  = readAtten1()
    atten2  = readAtten2()
    atten3  = readAtten3()
    atten4  = readAtten4()
    atten5  = readAtten5()
    atten6  = readAtten6()
    atten7  = readAtten7()
    atten8  = readAtten8()
    atten9  = readAtten9()
    atten10 = readAtten10()
    atten11 = readAtten11()
    atten12 = readAtten12()
    atten13 = readAtten13()
    atten14 = readAtten14()
    atten15 = readAtten15()
    atten16 = readAtten16()

    return render_template('attenuator.html', attens1=atten1, attens2=atten2, attens3=atten3, attens4=atten4, attens5=atten5, attens6=atten6, attens7=atten7, attens8=atten8, 
       attens9=atten9, attens10=atten10, attens11=atten11, attens12=atten12, attens13=atten13, attens14=atten14, attens15=atten15, attens16=atten16)

@mod.route('Atten1', methods = ['POST'])
def writeValue1():

    attenWrite = int(request.form.get('amountInput1'))
    writeAtten(1,attenWrite)

    return redirect('attenuator')

@mod.route('Atten2', methods = ['POST'])
def writeValue2():

    attenWrite = int(request.form.get('amountInput2'))
    writeAtten(2,attenWrite)

    return redirect('attenuator')

@mod.route('Atten3', methods = ['POST'])
def writeValue3():

    attenWrite = int(request.form.get('amountInput3'))
    writeAtten(3,attenWrite)

    return redirect('attenuator')

@mod.route('Atten4', methods = ['POST'])
def writeValue4():

    attenWrite = int(request.form.get('amountInput4'))
    writeAtten(4,attenWrite)

    return redirect('attenuator')

@mod.route('Atten5', methods = ['POST'])
def writeValue5():

    attenWrite = int(request.form.get('amountInput5'))
    writeAtten(5,attenWrite)

    return redirect('attenuator')

@mod.route('Atten6', methods = ['POST'])
def writeValue6():

    attenWrite = int(request.form.get('amountInput6'))
    writeAtten(6,attenWrite)

    return redirect('attenuator')

@mod.route('Atten7', methods = ['POST'])
def writeValue7():

    attenWrite = int(request.form.get('amountInput7'))
    writeAtten(7,attenWrite)

    return redirect('attenuator')

@mod.route('Atten8', methods = ['POST'])
def writeValue8():

    attenWrite = int(request.form.get('amountInput8'))
    writeAtten(8,attenWrite)

    return redirect('attenuator')

@mod.route('Atten9', methods = ['POST'])
def writeValue9():

    attenWrite = int(request.form.get('amountInput9'))
    writeAtten(9,attenWrite)

    return redirect('attenuator')

@mod.route('Atten10', methods = ['POST'])
def writeValue10():

    attenWrite = int(request.form.get('amountInput10'))
    writeAtten(10,attenWrite)

    return redirect('attenuator')

@mod.route('Atten11', methods = ['POST'])
def writeValue11():

    attenWrite = int(request.form.get('amountInput11'))
    writeAtten(11,attenWrite)

    return redirect('attenuator')

@mod.route('Atten12', methods = ['POST'])
def writeValue12():

    attenWrite = int(request.form.get('amountInput12'))
    writeAtten(12,attenWrite)

    return redirect('attenuator')

@mod.route('Atten13', methods = ['POST'])
def writeValue13():

    attenWrite = int(request.form.get('amountInput13'))
    writeAtten(13,attenWrite)

    return redirect('attenuator')

@mod.route('Atten14', methods = ['POST'])
def writeValue14():

    attenWrite = int(request.form.get('amountInput14'))
    writeAtten(14,attenWrite)

    return redirect('attenuator')

@mod.route('Atten15', methods = ['POST'])
def writeValue15():

    attenWrite = int(request.form.get('amountInput15'))
    writeAtten(15,attenWrite)

    return redirect('attenuator')

@mod.route('Atten16', methods = ['POST'])
def writeValue16():

    attenWrite = int(request.form.get('amountInput16'))
    writeAtten(16,attenWrite)

    return redirect('attenuator')

@mod.route('logout', methods=['GET'])
def logout():
    del session['logged_in']
    del session['user']
    return redirect('/')
    
@mod.route('register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        db = get_db()
        db.do_register(form.username.data, form.lastname.data,
                       form.firstname.data, form.email.data,
                       form.password.data, form.is_director.data)
        flash("Thanks for registering!")
        return redirect('/')
    return render_template('register.html', form=form)

@mod.route('pickup/', methods=['GET', 'POST'])
def pickup():
    if request.method == 'GET':
        return render_template('pickup.html')
    elif request.method == 'POST':
        if 'pickup' in request.form:
            pickup_day = request.form['pickup']
            db = get_db()
            result = db.do_pickup_query(pickup_day)
            if len(result) == 0:
                flash("No pickups found on this day.")
            print result
            return render_template('pickup.html', rows=result)
    # other methods are not supported
    return render_template('pickup.html')

@mod.route('pickup/<int:client_id>/', methods=['GET', 'POST'])
def family_pickup(client_id):
    if request.method == 'GET':
        ## BEGIN DB TRANSACTION
        db = get_db()
        client = db.client_lookup_by_id(client_id)
        if client is None:
            abort(404) # not found
        family_bag = db.do_family_bag_show(client_id)
        return render_template('family_pickup.html', client=client,
                               rows=family_bag)
    elif request.method == 'POST':
        ## BEGIN DB TRANSACTION
        db = get_db()
        db.do_family_bag_pickup(client_id)
        flash("Client {} has successfully picked up their bag.".format(client_id))
        return render_template('pickup.html')
    # other methods not supported
    return redirect('/pickup/')

@mod.route('clients/', methods=['GET'])
def clients():
    # nothing to do here but render the template response
    return render_template('clients.html')

@mod.route('clients/list/', methods=['GET', 'POST'])
def client_list():
    if request.method=='GET':
    ## BEGIN DB TRANSACTION
        db = get_db()
        result = db.get_clients()
        print result
        return render_template('client_list.html', clients=result)
    elif request.method=='POST':
        name = request.form.get('lastname')
        phone = request.form.get('phonenum')
        print "name: {} phone: {}".format(name, phone)
        db = get_db()
        clients = db.do_search_client(lastname=name, phone=phone)
        print clients
        return render_template('client_list.html', clients=clients)
    return render_template('client_list.html')

@mod.route('clients/new/', methods=['GET', 'POST'])
def new_client():
    # TODO
    db = get_db()
    aids = [(x['name'], x['name']) for x in db.do_get_aid()]
    bags = [(x['bag_name'], x['bag_name']) for x in db.do_attenuator()]
    form = ClientForm(request.form)
    form.aid.choices = aids
    form.bag.choices = bags
    if request.method == 'GET':
        return render_template('new_client.html', form=form)
    elif request.method == 'POST' and form.validate():
        db = get_db()
        db.do_new_client({
            'gender': 'M' if form.gender.data == 'Male' else 'F',
            'dob': form.birthdate.data,
            'start_date': form.start_date.data,
            'street': form.street.data,
            'city': form.city.data,
            'state': form.state.data,
            'zip': form.zipcode.data,
            'apartment': form.apartment_num.data,
            'firstname': form.first_name.data,
            'lastname': form.last_name.data,
            'phone': form.phone.data,
            'bag_name': form.bag.data,
            'pickup_day': form.pick_up_day.data
        })
        flash("New client created!")
        # hack - pull the client-id
        result = db._sqlconn.execute(''.join([
            'SELECT * FROM clients WHERE firstname = ? ',
            'AND lastname = ?'
        ]), (form.first_name.data, form.last_name.data))
        client_id = db._row_to_dict(result)[0]['id']
        if form.aid.data:
            db.do_client_add_aid(client_id, form.aid.data)
        return redirect('clients/family/{}/'.format(client_id))
    else:
        print "validation failed"
    return render_template('new_client.html', form=form)

@mod.route('clients/family/<int:client_id>/', methods=['GET', 'POST'])
def family_members(client_id):
    form = FamilyForm(request.form)
    if request.method == 'GET':
        db = get_db()
        family = db.do_get_family(client_id)
        return render_template('family_members.html', form=form, family=family, client_id=client_id)
    elif request.method == 'POST' and form.validate():
        db = get_db()
        db.do_add_family({
            'firstname': form.firstname.data,
            'lastname': form.lastname.data,
            'dob': form.dob.data,
            'gender': form.gender.data,
            'client_id': client_id
        })
        flash("Family member added!")
        return redirect('clients/family/{}/'.format(client_id))
    return render_template('family_members.html', form=form)

@mod.route('attenuator/', methods=['GET'])
def attenuator():
    return render_template('attenuator.html')

@mod.route('viewEditBag/<string:bagnameEnc>/', methods=['GET', 'POST'])
def view_edit_bag(bagnameEnc):
    bagname = base64.b16decode(bagnameEnc)
    if request.method=='GET':
    ## BEGIN DB TRANSACTION
        db = get_db()
        bag = db.do_view_bag(bagname)
    elif request.method=='POST':
        db = get_db()
        product_name=request.form['product_name']
        qty = request.form['qty']
        if qty == '0':
            print "removing a product"
            db.do_remove_product(bagname, product_name)
        else:
            db.do_edit_product_qty(bagname, product_name, qty)
        flash("Bag updated!")
        return redirect('viewEditBag/{}'.format(bagnameEnc))
    ## END DB TRANSACTION
    return render_template('viewEditBag.html', bag=bag, bagname=bagname, bagnameEnc=bagnameEnc)

@mod.route('editInventory/', methods=['POST'])
def editInventory():
    db = get_db()
    #manufacturer = request.form['manufacturer']
    location = request.form['location']
    serialnum = request.form['serialnum']
    db.do_edit_product_location(location, serialnum)
    flash("Location updated!")
    return redirect('inventory/list/')
    ## END DB TRANSACTION
    return render_template('inventory_list.html')

@mod.route('dropoff/', methods=['GET', 'POST'])
def dropoff():
    form = DropoffForm(request.form)
    if request.method == 'GET':
        return render_template('dropoff.html', form=form)
    elif request.method == 'POST' and form.validate():
        db = get_db()
        success = db.do_drop_off([{
            'source': form.source.data,
            'product': form.product.data,
            'qty': form.qty.data
        }])
        if not success:
            flash("Product does not exist in the database!")
        else:
            flash("Dropoff complete!")
        return redirect('dropoff/')
    return render_template('dropoff.html', form=form)

@mod.route('inventory/', methods=['GET'])
def inventory():
    return render_template('inventory.html')

@mod.route('inventory/list/', methods=['GET', 'POST'])
def product_list():
    if request.method=='GET':
        ## BEGIN DB TRANSACTION
        db = get_db()
        products = db.do_list_products()
        return render_template('inventory_list.html', products=products)
    elif request.method=='POST':
        product_type=request.form['product_type']
        ## BEGIN DB TRANSACTION
        db = get_db()
        products = db.do_search_products(product_type)
        return render_template('inventory_list.html', products=products)
    return render_template('inventory_list.html')

@mod.route('inventory/new/', methods=['GET', 'POST'])
def new_product():
    form = NewProductForm(request.form)
    if request.method == 'GET':
        return render_template('new_inventory.html', form=form)
    elif request.method == 'POST' and form.validate():
        db = get_db()
        db.do_add_new_product({
            'manufacturer': form.manufacturer.data,
            'model': form.model.data,
            'serialnum': form.serialnum.data,
            'location': form.location.data
        })
        flash("Product added!")
        return redirect('/inventory/new/')
    return render_template('new_inventory.html', form=form)

@mod.route('reports/', methods=['GET'])
def reports():
    # nothing to do but render response
    return render_template('reports.html')

@mod.route('reports/monthly_report/', methods=['GET'])
def monthly_report():
    db = get_db()
    report = db.do_monthly_service_report()
    return render_template('monthly_report.html', row=report)

@mod.route('reports/grocery_report/', methods=['GET'])
def grocery_report():
    db = get_db()
    report = db.do_grocery_list_report()
    return render_template('grocery_report.html', rows=report)
