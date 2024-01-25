from flask import Flask, render_template, request

app = Flask(__name__)



app = Flask'(__na


app = 
@app.route('/')
def ana_sayfa():
    
    retu

 
return render_template('index.html')

@app.route('/kayit', methods=['POST'])
def kayit():
    if request.method == 'POST':
        kullanici_adi = request.form[
        kullanici_adi = request.

        kullanici_adi =

        kullan

    
'username']
        sifre = request.form[
        sifre = reques

        sifre

   
'password']
        
       
# Diğer bilgileri de alabilirsiniz

        

   
# Burada veritabanına kaydetme veya işleme kodları eklenebilir

        

        


  
return f'{kullanici_adi}, başarıyla kaydedildi!'



i
if __name__ == '__main__':
    app.run(debug=
    app.r

  
True)