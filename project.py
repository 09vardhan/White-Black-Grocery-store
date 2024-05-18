from flask import Flask,request,render_template,url_for,redirect,flash,abort,session,Response
import mysql.connector
from flask_session import Session
from itsdangerous import URLSafeTimedSerializer
from stoken import token
from key import secret_key,salt,salt2,salt3
from cmail import sendmail
from otp import adotp
import os
from io import BytesIO
import re
import stripe
import pdfkit
stripe.api_key='sk_test_51MMsHhSGj898WTbYXSx509gD14lhhXs8Hx8ipwegdytPB1Bkw0lJykMB0yGpCux95bdw1Gk9Gb9nJIWzPEEDxSqf00GEtCqZ8Y'
mydb=mysql.connector.connect(host='localhost',user='root',password='anusha@1999',db='ecom')


app=Flask(__name__)

app.secret_key=secret_key
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

app.config['SESSION_TYPE']='filesystem'
'''user=os.environ.get('RDS_USERNAME')
db=os.environ.get('RDS_DB_NAME')
password=os.environ.get('RDS_PASSWORD')
host=os.environ.get('RDS_HOSTNAME')
port=os.environ.get('RDS_PORT')
with mysql.connector.connect(host=host,port=port,user=user,password=password,db=db) as conn:
    cursor=conn.cursor()
    cursor.execute('create table if not exists users(user_id binary(16),user_name varchar(25) primary key,u_mobile bigint,email varchar(20) unique not null,gender enum("M","F","NAN"),address varchar(256),password varchar(20))')
    cursor.execute("create table if not exists admindetails(admin_id varchar(6) not null unique,admin_name varchar(20),admin_email varchar(50) primary key,admin_mobile bigint not null unique,password varchar(8))")
    cursor.execute("create table if not exists additems(item_id binary(16) primary key,item_name longtext,dis longtext not null,qyt int not null,category enum('Electronics','Grocery','Fashion','Home'),price int not null,addedby varchar(50),imgid varchar(10),foreign key(addedby) references admindetails(admin_email))")
    cursor.execute("create table if not exists reviews(itemid binary(16),user varchar(25),title tinytext,review text,rating int,date datetime default current_timestamp(),primary key(itemid,user))")
    cursor.execute("create table if not exists orders(ordid bigint primary key auto_increment,itemid binary(16),item_name longtext,qyt int,total_price bigint,user varchar(25),foreign key(itemid) references additems(item_id),foreign key(user) references users(user_name))")
    cursor.execute("create table if not exists contactus(name varchar(30),emailid varchar(40),message tinytext)")
mydb=mysql.connector.connect(host=host,user=user,password=password,db=db,port=port)'''
Session(app)
@app.route('/')
def index():
    return render_template('welcome.html')
@app.route('/homepage')
def home():
    cursor=mydb.cursor(buffered=True)
    cursor.execute("select bin_to_uuid(item_id),item_name,dis,qyt,category,price,imgid from additems")
    items=cursor.fetchall()
    return render_template('home1.html',items=items)
@app.route('/signup',methods=['GET','POST'])
def usignup():
    if request.method=='POST':
        user=request.form['name']
        mobile=request.form['mobile']
        email=request.form['email']
        address=request.form['address']
        gender=request.form['gender']
        password=request.form['password']
        #print(user,mobile,email,address,gender,password)
        try:
            cursor=mydb.cursor(buffered=True)
            cursor.execute('select count(*) from users where email=%s',[email])
            count=cursor.fetchone()[0]
            print(count)
            if count==1:
                raise Exception
        except Exception as e:
            flash('User alredy registered')
            return redirect(url_for('home'))
        else:
            data={'user':user,'email':email,'mobile':mobile,'address':address,'gender':gender,'password':password}
            subject='The confirmation link has sent to Email'
            body=f"Click the link to confirm{url_for('confirm',token=token(data,salt=salt),_external=True)}"
            sendmail(to=email,subject=subject,body=body)
            flash('Link has sent to this Mail')
            return redirect(url_for('login'))
    return render_template('signup.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if session.get('user'):
        return redirect(url_for('home'))
    if request.method=='POST':
        user=request.form['username']
        password=request.form['password']
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select user_name,password from users where user_name=%s and password=%s',[user,password])
        count=cursor.fetchone()
        if count==(user,password):
            session['user']=user
            if not session.get(user):
                session[user]={}
            return redirect(url_for('home'))
    return render_template('login.html')
@app.route('/confirm/<token>')
def confirm(token):
    try:
        serializer=URLSafeTimedSerializer(secret_key)
        data=serializer.loads(token,salt=salt,max_age=180)
    except Exception as e:
        abort(404,'Link expired')
    else:
        cursor=mydb.cursor(buffered=True)
        cursor.execute('insert into users(user_id,user_name,u_mobile,email,gender,address,password) values(uuid_to_bin(uuid()),%s,%s,%s,%s,%s,%s)',[data['user'],data['mobile'],data['email'],data['gender'],data['address'],data['password']])
        mydb.commit()
        cursor.close()
        flash('Details Registered successfully')
        return redirect(url_for('login'))
@app.route('/logout')
def logout():
    if session.get('user'):
        session.pop('user')
        return redirect(url_for('login'))
    return redirect(url_for('login'))
@app.route('/forgot',methods=['GET','POST'])
def forgot():
    if request.method=='POST':
        email=request.form['id']
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select count(*) from users where email=%s',[email])
        count=cursor.fetchone()[0]
        cursor.close()
        try:
            if count!=1:
                raise Exception
        except Exception as e:
            flash('Pls Register for the application')
            return redirect(url_for('index'))
        else:
            subject='Reset link for ecom application'
            body=f"The reset link for ecom application: {url_for('uforgot',token=token(email,salt=salt2),_external=True)}"
            sendmail(to=email,subject=subject,body=body)
            flash('Reset Link has sent to give email pls check.')
            return redirect(url_for('forgot'))
    return render_template('forgot.html')
@app.route('/uforgot/<token>',methods=['GET','POST'])
def uforgot(token):
    try:
        serializer=URLSafeTimedSerializer(secret_key)
        data=serializer.loads(token,salt=salt2,max_age=180)
    except:
        abort(404,'Reset link expired')
    else:
        if request.method=='POST':
            npassword=request.form['npassword']
            cpassword=request.form['cpassword']
            if npassword==cpassword:
                cursor=mydb.cursor(buffered=True)
                cursor.execute('update users set password=%s where email=%s',[npassword,data])
                mydb.commit()
                cursor.close()
                flash('Password has updated')
                return redirect(url_for('login'))
            else:
                flash('Mismatched  confirmation password')
                return render_template('newpassword.html')
        return render_template('newpassword.html')
@app.route('/admincreate',methods=['GET','POST'])
def admincreate():
    if request.method=='POST':
        a_id=adotp()
        admin=request.form['name']
        aemail=request.form['email']
        amobile=request.form['mobile']
        password=request.form['password']
        try:
            cursor=mydb.cursor(buffered=True)
            print('hi')
            cursor.execute('select count(*) from admindetails where admin_email=%s',[aemail])
            count=cursor.fetchone()[0]
            print(count)
            if count==1:
                raise Exception
        except Exception as e:
            flash('User alredy existed')
            return redirect(url_for('index'))
        else:
            serializer=URLSafeTimedSerializer(secret_key)
            data=serializer.dumps(a_id,salt=salt3)
            subject='OTP for ecom application'
            body=f"This is the otp for your account creation: {a_id}"
            sendmail(to=aemail,subject=subject,body=body)
            flash('The otp has sent to given mail')
            return redirect(url_for('adminverify',data=data,admin=admin,aemail=aemail,amobile=amobile,password=password))
        
    return render_template('adminsignup.html') 
@app.route('/adminverify/<data>/<admin>/<aemail>/<amobile>/<password>',methods=['GET','POST'])
def adminverify(data,admin,aemail,amobile,password):
    try:
        serializer=URLSafeTimedSerializer(secret_key)
        otp=serializer.loads(data,salt=salt3,max_age=180)
        
    except:
        abort(404,'OTP has expired')
    else:
        if request.method=='POST':
            print(otp)
            uotp=request.form['adminotp']
            print(uotp)
            if otp==uotp:
                cursor=mydb.cursor(buffered=True)
                cursor.execute('insert into admindetails(admin_id,admin_name,admin_mobile,admin_email,password) values(%s,%s,%s,%s,%s)',[uotp,admin,amobile,aemail,password])
                mydb.commit()
                cursor.close()
                flash('Details Registered successfully')
                return redirect(url_for('adminlogin'))
    return render_template('adminotp.html')
@app.route('/adminlogin',methods=['GET','POST'])
def adminlogin():
    if session.get('user'):
        return redirect(url_for('admindash'))
    if request.method=='POST':
        auser=request.form['email']
        password=request.form['password']
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select admin_email,password from admindetails where admin_email=%s and password=%s',[auser,password])
        count=cursor.fetchone()
        if count==(auser,password):
            session['auser']=auser
            return redirect(url_for('admindash'))
    return render_template('adminlogin.html')
@app.route('/aforgot',methods=['GET','POST'])
def aforgot():
    if request.method=='POST':
        email=request.form['id']
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select count(*) from admindetails where admin_email=%s',[email])
        count=cursor.fetchone()[0]
        cursor.close()
        try:
            if count!=1:
                raise Exception
        except Exception as e:
            flash('Pls Register for the application')
            return redirect(url_for('index'))
        else:
            subject='Admin Reset link for ecom application'
            body=f"The reset link for ecom application: {url_for('averify',token=token(email,salt=salt2),_external=True)}"
            sendmail(to=email,subject=subject,body=body)
            flash('Reset Link has sent to give email pls check.')
            return redirect(url_for('aforgot'))
    return render_template('adminforgot.html')
@app.route('/averify/<token>',methods=['GET','POST'])
def averify(token):
    try:
        serializer=URLSafeTimedSerializer(secret_key)
        data=serializer.loads(token,salt=salt2,max_age=180)
    except:
        abort(404,'Reset link expired')
    else:
        if request.method=='POST':
            npassword=request.form['npassword']
            cpassword=request.form['cpassword']
            if npassword==cpassword:
                cursor=mydb.cursor(buffered=True)
                cursor.execute('update admindetails set password=%s where admin_email=%s',[npassword,data])
                mydb.commit()
                cursor.close()
                flash('Password has updated')
                return redirect(url_for('adminlogin'))
            else:
                flash('Mismatched  confirmation password')
                return render_template('adminnewpassword.html')
    return render_template('adminnewpassword.html')
@app.route('/admindashboard')
def admindash():
    return render_template('admindashboard.html')
@app.route('/alogout')
def alogout():
    if session.get('auser'):
        session.pop('auser')
        return redirect(url_for('adminlogin'))
    return redirect(url_for('login'))
@app.route('/additems',methods=['GET','POST'])
def additems():
    if session.get('auser'):
        if request.method=='POST':
            item_name=request.form['name']
            desc=request.form['desc']
            qyt=request.form['qty']
            category=request.form['category']
            print(category)
            price=request.form['price']
            addedby=session.get('auser')
            image=request.files['image']
            filename=adotp()+'.jpg'
            path=os.path.dirname(os.path.abspath(__file__))
            static_path=os.path.join(path,'static')
            image.save(os.path.join(static_path,filename))
            cursor=mydb.cursor(buffered=True)
            cursor.execute('insert into additems(item_id,item_name,dis,qyt,category,price,addedby,imgid) values(uuid_to_bin(uuid()),%s,%s,%s,%s,%s,%s,%s)',[item_name,desc,qyt,category,price,addedby,filename])
            mydb.commit()
            cursor.close()
            flash('Item added successfully')
            return redirect(url_for('additems'))
    return render_template('items.html')
@app.route('/pstatus')
def pstatus():
    if session.get('auser'):
        print(session.get('auser'))
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select bin_to_uuid(item_id),item_name,dis,qyt,category,price from additems where addedby=%s',[session.get('auser')])
        items=cursor.fetchall()
        print(items)
        cursor.close()
        return render_template('status.html',items=items)
    return redirect(url_for('adminlogin'))
@app.route('/update/<itemid>',methods=['GET','POST'])
def update(itemid):
    if session.get('auser'):
        print(itemid)
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select item_name,dis,qyt,category,price from additems where item_id=uuid_to_bin(%s)',[itemid])
        data=cursor.fetchone()
        cursor.close()
        if request.method=='POST':
            item_name=request.form['name']
            desc=request.form['desc']
            qyt=request.form['qty']
            category=request.form['category']
            price=request.form['price']
            cursor=mydb.cursor(buffered=True)
            cursor.execute('update additems set item_name=%s,dis=%s,qyt=%s,category=%s,price=%s where item_id=uuid_to_bin(%s)',[item_name,desc,qyt,category,price,itemid])
            mydb.commit()
            cursor.close()
            flash('Item details Updated successfully')
            return redirect(url_for('pstatus'))
    return render_template('updateproducts.html',data=data)
@app.route('/pdelete/<itemid>')
def delete(itemid):
    cursor=mydb.cursor(buffered=True)
    cursor.execute('delete from additems where item_id=uuid_to_bin(%s) and addedby=%s',[itemid,session.get('auser')])
    mydb.commit()
    cursor.close()
    return redirect(url_for('pstatus'))
@app.route('/contactus',methods=['GET','POST'])
def contactus():
    if request.method=='POST':
        name=request.form['name']
        emailid=request.form['emailid']
        msg=request.form['msg']
        cursor=mydb.cursor(buffered=True)
        cursor.execute('insert into contactus(name,emailid,message) values(%s,%s,%s)',[name,emailid,msg])
        mydb.commit()
        cursor.close()
        flash('report sent successfully')
        return redirect(url_for('contactus'))
    return render_template('contactus.html')
@app.route('/readcontactus')
def readcontact():
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select * from contactus')
    contact=cursor.fetchall()
    return render_template('readcontactus.html',contact=contact)
@app.route('/dashboard/<category>')
def dashboard(category):
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select  bin_to_uuid(item_id),item_name,dis,qyt,category,price,imgid from additems where category=%s',[category])
    items=cursor.fetchall()
    return render_template('dashboard.html',items=items)
@app.route('/dashboardpage')
def allitems():
    cursor=mydb.cursor(buffered=True)
    cursor.execute("select bin_to_uuid(item_id),item_name,dis,qyt,category,price,imgid from additems")
    items=cursor.fetchall()
    return render_template('dashboard.html',items=items)
@app.route('/cart/<itemid>/<name>/<desc>/<category>/<price>/<imgid>')
def cart(itemid,name,desc,category,price,imgid):
    if not session.get('user'):
        return redirect(url_for('login'))
    print(session.get('user'))
    if itemid not in session[session.get('user')]:
        session[session.get('user')][itemid]=[name,desc,1,price,imgid]
        session.modified=True
        flash(f'{name} added to cart')
        return redirect(url_for('dashboard',category=category))
    session[session.get('user')][itemid][2]+=1
    flash('Item already existed')
    return redirect(url_for('dashboard',category=category))
@app.route('/viewcart')
def viewcart():
    if not session.get('user'):
        return redirect(url_for('login'))
    items=session.get(session.get('user')) if session.get(session.get('user')) else 'empty' 
    if items=='empty':
        return render_template('cart2.html')

    print(items)
    return render_template('cart.html',items=items)
@app.route('/rem/<item>')
def rem(item):
    if session.get('user'):
        session[session.get('user')].pop(item)
        return redirect(url_for('viewcart'))
    return redirect(url_for('login'))
@app.route('/dis/<itemid>')
def dis(itemid):
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select bin_to_uuid(item_id),item_name,dis,category,price,imgid from additems where item_id=uuid_to_bin(%s)',[itemid])
    items=cursor.fetchone()
    cursor.close()
    return render_template('discription.html',items=items)
@app.route('/writereview/<itemid>',methods=['GET','POST'])
def wreview(itemid):
    if session.get('user'):
        if request.method=='POST':
            user=session.get('user')
            title=request.form['title']
            desc=request.form['decs']
            rate=request.form['rate']
            cursor=mydb.cursor(buffered=True)
            cursor.execute('insert into reviews(itemid,user,title,review,rating) values(uuid_to_bin(%s),%s,%s,%s,%s)',[itemid,user,title,desc,rate])
            mydb.commit()
            cursor.close()
            flash('Thank you for the feedback')
        return render_template('review.html')
    return redirect(url_for('login'))
@app.route('/search',methods=['GET','POST'])
def search():
    if request.method=='POST':
        name=request.form['search']
        strg=['A-Za-z0-9']
        pattern=re.compile(f'^{strg}', re.IGNORECASE)
        if pattern.match(name):
            cursor=mydb.cursor(buffered=True)
            cursor.execute('select bin_to_uuid(item_id),item_name,dis,qyt,category,price from additems where item_name LIKE %s', [name + '%'])
            data=cursor.fetchall()
            cursor.close()
            return render_template('dashboard.html', items=data)
        else:
            flash('result not found')
    return render_template('home1.html')
@app.route('/readreview/<itemid>')
def rreview(itemid):
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select itemid,user,title,review,rating,date from reviews where itemid=uuid_to_bin(%s)',[itemid])
    reviews=cursor.fetchall()
    cursor.close()
    return render_template('readreview.html',reviews=reviews)
@app.route('/pay/<itemid>/<name>/<int:price>',methods=['POST'])
def pay(itemid,price,name):
    if session.get('user'):
        print(itemid)
        q=int(request.form['qty'])
        username=session.get('user')
        total=price*q
        checkout_session=stripe.checkout.Session.create(
            success_url=url_for('success',itemid=itemid,name=name,q=q,total=total,_external=True),
            line_items=[
                {
                    'price_data': {
                        'product_data': {
                            'name': name,
                        },
                        'unit_amount': price*100,
                        'currency': 'inr',
                    },
                    'quantity': q,
                },
                ],
            mode="payment",)
        return redirect(checkout_session.url)
    else:
        return redirect(url_for('login'))
@app.route('/sucess/<itemid>/<name>/<q>/<total>')
def success(itemid,name,q,total):
    if session.get('user'):
        user=session.get('user')
        print(user)
        cursor=mydb.cursor(buffered=True)
        cursor.execute('insert into orders(itemid,item_name,qyt,total_price,user) values(uuid_to_bin(%s),%s,%s,%s,%s)',[itemid,name,q,total,user])
        mydb.commit()
        cursor.close()
        return redirect(url_for('orders'))
    return redirect(url_for('login'))
@app.route('/orders')
def orders():
    if session.get('user'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select * from orders where user=%s',(session['user'],))
       
        orders=cursor.fetchall()
        return render_template('orders.html',orders=orders)
@app.route('/billdetails/<ordid>.pdf')
def invoice(ordid):
    # Make a PDF straight from HTML in a string.
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select * from orders where ordid=%s',[ordid])
    orders=cursor.fetchone()
    username=orders[5]
    oname=orders[2]
    qty=orders[3]
    cost=orders[4]
    cursor.execute('select user_name,u_mobile,address,email from users where user_name=%s',[username])
    data=cursor.fetchone()
    uname=data[0]
    uaddress=data[2]
    uphnumber=data[1]
    html=render_template('bill.html', uname=uname,uaddress=uaddress,uphnumber=uphnumber,oname=oname,qty=qty,cost=cost)
    #return render_pdf(HTML(string=html))
    pdf = pdfkit.from_string(html, False, configuration=config)
    response = Response(pdf, content_type='application/pdf')
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    return response
if __name__=='__main__':    
    app.run()