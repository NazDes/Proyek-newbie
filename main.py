from flask import Flask
import random
app = Flask(__name__)

fakta = ['Kecanduan main game bisa membuat kamu lupa waktu', 
         'Kecanduan .......',
         'Kecanduan .......']

@app.route('/')
def home ():
    return '<h1>INI HALAMAN UTAMA</h1><a href="/random_facts">Klik untuk melihat fakta</a><h2></h2><a href="/ALAMAT">Link limited</a>'

@app.route("/ALAMAT")
def FUNCTION_NAME():
    return '<h1>Password generator</h1><a href="/">Back to home</a>'

@app.route("/random_facts")
def random_facts():
    return f'<p>Hello, World!</p><br><p>{random.choice(fakta)}</p><a href="/">Back to Home</a>'
app.run(debug=True)
