from tkinter import Variable
from flask import Flask, render_template, request, Response,url_for, redirect, jsonify
import database as dbase
from user.models import Agent

db = dbase.dbConnection()

app = Flask(__name__, static_url_path="/static", static_folder='static')

@app.route('/')
def home():
    agents = db['agents']
    agentsReceived = agents.find()
    return render_template('index.html', agents = agentsReceived)

@app.route('/agent', methods=['POST'])
def addAgent():
    agents = db['agents']
    name = request.form['name']
    lastname = request.form['lastname']
    user = request.form['user']
    phone = request.form['phone']
    email = request.form['email']
    password = request.form['password']
    address = request.form['address']
    document_type = request.form['document_type']
    document_number = request.form['document_number']
    rol = request.form['rol']

    if name and lastname and user and phone and password and address and document_type and document_number and rol and email:
        agent = Agent(name, lastname, user, phone, email, password, address, document_type, document_number, rol)

        agents.insert_one(agent.toDBCollection())
        response = jsonify({
            'name': name,
            'lastname': lastname,
            'user': user,
            'phone': phone,
            'email': email,
            'password': password,
            'address': address,
            'document_type': document_type,
            'doument_number': document_number, 
            'rol': rol
        })
        return redirect(url_for('home'))

@app.route('/edit/<string:agent_name>')
def edit(agent_name):
    agents = db['agents']
    agents = db['agents']
    name = request.form['name']
    lastname = request.form['lastname']
    user = request.form['user']
    phone = request.form['phone']
    email = request.form['email']
    password = request.form['password']
    address = request.form['address']
    document_type = request.form['document_type']
    document_number = request.form['document_number']
    rol = request.form['rol']

    if name and lastname and user and phone and password and address and document_type and document_number and rol and email:
        agents.update_one({'name' : product_name}, {'$set' : {'name' : name, 'price' : price, 'quantity' : quantity}})
        response = jsonify({'message' : 'Producto ' + product_name + ' actualizado correctamente'})
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=5000)