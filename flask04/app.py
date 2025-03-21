# app.py
from flask import Flask, render_template
from producto import Producto
from flask import request
from flask import Response
from flask import redirect, url_for

app = Flask(__name__)

productos = [Producto("Coca", 25), Producto("Fanta", 15), Producto("Pepsi", 20), Producto("Fanta", 16), Producto("Fanta", 17), Producto("Fanta", 18)]

@app.route('/')
def inicio():
    #productos = [Producto("Coca", 25), Producto("Pepsi", 20), Producto("Fanta", 15)]
    return render_template('producto.html', productos=productos)

@app.route('/editar/<producto>/<precio>')
def editar(producto, precio):
    #Recuperar el producto
    return render_template('editar.html', producto = producto, precio = precio)

@app.route('/guardar', methods=['POST'])
def guardar():
    n= request.form.get('nombre')
    p= request.form.get('precio')
    print(n,p)
    i = 0
    for e in productos:
        if e.nombre == n:
            productos[i] = Producto(n,p)
            print(f"{e.nombre} {e.precio}")
        i+=1
    #return Response("guardado", headers={'Location': '/'}, status=302)
    return redirect(url_for('inicio'))

@app.route('/crear', methods=['POST'])
def crear():
    n = request.form.get('nombre')
    p = request.form.get('precio')
    productos.append(Producto(n,p))
    return Response("creado", headers={'Location': '/'}, status=302)

@app.route('/eliminar/<producto>/<int:precio>')
def eliminar(producto, precio):
    i = 0
    for e in productos:
        if e.nombre == producto and e.precio == precio:
            productos.pop(i)
        i+=1
    return Response("eliminado", headers={'Location': '/'}, status=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
