# PythonOCR-FlaskWebProject
PDF dosyaları içindeki yazıların string olarak elde edilmesini sağlar. Api uygulaması olarak geliştirilmiştir. Diğer tüm platformlardan istek yaparak pdf dosyalardan metin çıkartılıp alınabilir.


Pytesseract : “TesseractNotFound Error: tesseract is not installed or it's not in your path”,hatası alırsanız yapmanız gerekenler



Windows için
1 - Bilgisayarınızda Tesseract OCR kurulu olmalıdır.
Buradan al. https://github.com/UB-Mannheim/tesseract/wiki
Uygun sürümü buradan indirin.

2 - Tesseract yolunu  Sistem değişkenlerine ekleyin

3 - pip install pytesseract ve pip install tesseract

4 - Bu satırı python komut dosyasına ekleyin (proje içersinde eklidir.)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR' ^ sizin kurduğunuz dizin neresi ise o dizini r ' ' arasına eklemelisiniz.

5 - Kodu tekrar çalıştırın.
