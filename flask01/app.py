from flask import Flask

app = Flask(__name__)

def hola():
    return "Hola Mundo"

def adios():
    return "Adiós Mundo"

@app.route('/')
def mensaje():
    return f"{hola()} {adios()}"

@app.route('/hola')
def hola_mundo():
    return '<h1 style="color: red;">Hola Mundo</h1>'

@app.route('/json')
def json():
    return '{"nombre": "Christian"}'

@app.route('/xml')
def xml():
    return '<?xml version="1.0"?><nombre>Christian</nombre>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    