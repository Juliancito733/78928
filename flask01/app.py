from flask import Flask, Response

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
    return Response('{"nombre": "Christian"}', mimetype='application/json')

@app.route('/xml')
def xml():
    xml = '<?xml version="1.0"?>' \
    '<persona>' \
    '   <nombre>Christian</nombre>' \
    '</persona>'
    return Response(xml, mimetype='application/xml')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    