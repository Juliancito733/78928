# app.py
from flask import Flask, render_template
from modelos import Producto

app = Flask(__name__)

@app.route('/')
def inicio():
    productos = [Producto("Coca", 25), Producto("Pepsi", 20), Producto("Fanta", 15)]
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
