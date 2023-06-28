from flask import render_template, request, redirect, url_for
from flask_jwt_extended import create_access_token
from database import conexion as db

# Ruta para el formulario de inicio de sesión
def login():
    userDict = {}
    if request.method == 'POST':
        # Verificar las credenciales de inicio de sesión
        username = request.form['username']
        password = request.form['password']

        # Aquí puedes realizar la validación de las credenciales
        # Comparar con una base de datos o autenticar de alguna otra manera
        try:
            with db:
                with db.cursor() as cursor:
                    sentencia = "SELECT * FROM usuario WHERE username = %s AND password = %s"
                    valores = (username, password)
                    cursor.execute(sentencia, valores)
                    user = cursor.fetchone()

                    if user:
                        # Autenticación exitosa, obtener los valores necesarios
                        nombre_usuario = user[1]
                        contrasenia = user[2]

                        if username == nombre_usuario and password == contrasenia:
                        # Pasar los valores a la plantilla para mostrarlos
                            print(nombre_usuario, contrasenia)
                            access_token = create_access_token(identity=username)
                            print(access_token)
                            return {'access_token': access_token}
            
        except Exception as e:
            print(f'Ocurrió un error al verificar los datos del usuario, usuario o contraseña inválidos: {e}')
        finally:
            cursor.close()
            
    return render_template('login.html')