# PythonOCR-FlaskWebProject
<h3> PDF dosyaları içindeki yazıların string olarak elde edilmesini sağlar. Api uygulaması olarak geliştirilmiştir. Diğer tüm platformlardan istek yaparak pdf dosyalardan metin çıkartılıp alınabilir.
</h3

<h2>Pytesseract : “TesseractNotFound Error: tesseract is not installed or it's not in your path”,hatası alırsanız yapmanız gerekenler</h2>


### Windows için Kurulum

 ### 1 
                   
> Bilgisayarınızda Tesseract OCR kurulu olmalıdır.
[Links](https://github.com/UB-Mannheim/tesseract/wiki)
Uygun sürümü buradan indirin.



### 2 
                    
> Tesseract yolunu  Sistem değişkenlerine ekleyin 
nasıl ekleneceğini bilmiyorsanız bu videoyu izleyin [Links](https://onedrive.live.com/?authkey=%21AP5Ln23ZkVqfwBQ&cid=7D42363E6971485E&id=7D42363E6971485E%213115&parId=root&o=OneUp)

### 3 
               
> pip install pytesseract 
> pip install tesseract
> pip install pdf2image
> pip install flask_sqlalchemy
> pip install flask_httpauth
> pip install passlib

komutlarını çalıştırın


### 4 
                    
> Bu satırı kodlarınıza ekleyin (proje içersinde eklidir.)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

### 4 
> Bu satırı kodlarınıza ekleyin (proje içersinde eklidir.)
 
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR' 

sizin kurduğunuz dizin neresi ise o dizini r ' ' arasına eklemelisiniz.

### 5 -
                    
> Kodu tekrar çalıştırın.>


### Not: out_text.txt  dosyasında pdf dosyasının içeriğini göreceksiniz. Eğer Türkçe karakter sorunu var ise karakter kodlamasını UTF-8 yapmalısınız.


# Python SQLAlchemy Kurulumu
pip install SQLAlchemy==1.3.11
