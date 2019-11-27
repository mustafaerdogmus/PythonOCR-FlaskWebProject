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


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'

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
