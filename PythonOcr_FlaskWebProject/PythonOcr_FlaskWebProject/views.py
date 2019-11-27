"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from PythonOcr_FlaskWebProject import app
from flask import request
import pytesseract 
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import sys 
from pdf2image import convert_from_path 
import os 

#db auth
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from flask import Flask, abort, request, jsonify, g, url_for


# extensions
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@app.route('/api/test', methods=['GET'])
def test():
    mustafa = "asdfasdf"

@app.route('/api/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)    # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(400)    # existing user
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return (jsonify({'username': user.username}), 201,
            {'Location': url_for('get_user', id=user.id, _external=True)})

@app.route('/api/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})


@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.username})
@app.route('/')
@app.route('/home')
def home():
   
    try:
     # pdf dosya(larının) bulunduğu dizin
     basePath = "C:\\Users\\BIM-ME\\source\\repos\\PythonOcr_FlaskWebProject\\"
    
     pdf_file_path = os.path.join(basePath, "d.pdf")
     pages = convert_from_path(pdf_file_path, 500) 
    
     #  PDF sayfasının resimlerini sırasıyla saklamak için sayaç değişkeni tanımlama
     image_counter = 1
     for page in pages: 
     
          # PDF'nin her sayfası için dosya adını JPG olarak tanımlama
          # PDF page 1 -> page_1.jpg
          # PDF page 2 -> page_2.jpg
          # PDF page 3 -> page_3.jpg
          # ....
          # PDF page n -> page_n.jpg
          filename = "page_" + str(image_counter) + ".jpg"
          # pdf sayfasının resmini kaydetme
          page.save(filename, 'JPEG') 
          # sayfa sayısını sayaç artırma
          image_counter = image_counter + 1
          """Renders the home page."""
          filelimit = image_counter-1
          # işlem sonucu metnin kaydedileceği dosya tanımlaması
          outfile = "out_text.txt"
            
          # Dosyayı append modu ile açıyoruz ve tüm pdf lerin metinleri tek bir dosyaya yazılacak
          f = open(outfile, "a") 
            
          for i in range(1, filelimit + 1): 
            
             filename = "page_"+str(i)+".jpg"              
             # Pytesseract kullanarak görüntüyü metin olarak alır text değişkenine atar.
             text = str(((pytesseract.image_to_string(Image.open(filename),lang='tur')))) 
             text = text.replace('-\n', '')     
             # metin olarak alınan açılan dosyaya yazılır
             f.write(text) 
     # yazma işleminden sonra dosya kapatılır.
     f.close() 
    except Exception as error:
     print("error " + error)
    

    return render_template('index.html',
        title='Home Pageeee',
        year=datetime.now().year,message=text)
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.')
