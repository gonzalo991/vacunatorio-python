from flask import Flask, render_template, request, redirect, url_for, session
import os
from api import home, agregar_paciente, borrar_paciente, editar_paciente
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from login import login
from database import conexion as db


template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'clave_secreta'  # Cambia esto por una clave secreta más segura
app.config['JWT_SECRET_KEY'] = 'clave_secreta_jwt'  # Cambia esto por una clave secreta para JWT
jwt = JWTManager(app)


# Rutas

# Home
app.route('/')(home)

# Agregar Paciente
app.route('/agregar_paciente', methods=['POST'])(agregar_paciente)

#Borrar paciente
app.route('/borrar_paciente/<int:id>', methods=['DELETE'])(borrar_paciente)

#Editar paciente
app.route('/editar_paciente/<int:id>', methods=['POST'])(editar_paciente)

#Login
app.route('/login', methods=['GET','POST'])(login)

@app.route('/bienvenido')
@jwt_required()
def bienvenido():
    username = get_jwt_identity()
    return f'Hola, {username}! <a href="/logout">Cerrar sesión</a>'

if __name__ == '__main__':
    app.run(debug=True, port=5000)