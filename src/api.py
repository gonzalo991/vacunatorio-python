from flask import render_template, redirect, request, url_for
from database import conexion as db

def home():
    insertObject = []
    try:
        with db: 
            with db.cursor() as cursor:
                sentencia = 'SELECT * FROM paciente'
                cursor.execute(sentencia)
                myresult = cursor.fetchall()
                
                columNames = [column[0] for column in cursor.description]
                for record in myresult:
                    insertObject.append(dict(zip(columNames, record)))
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    finally:
        cursor.close()
        return render_template('index.html', data = insertObject) 

def agregar_paciente():
    nombre = request.form['nombre']
    segundo_nombre = request.form['segundo_nombre']
    apellido = request.form['apellido']
    nro_dni = request.form['nro_dni']
    fecha_nacimiento = request.form['fecha_nacimiento']
    dosis = request.form['dosis']
    fecha_aplicacion = request.form['fecha_aplicacion']
    centro_salud = request.form['centro_salud']
    nombre_vacuna = request.form['nombre_vacuna']
    lote_vacuna = request.form['lote_vacuna']
    try:
        with db:
            with db.cursor() as cursor:
                sentencia = 'INSERT INTO paciente (nombre, segundo_nombre, apellido,nro_dni,fecha_nacimiento,dosis,fecha_aplicacion, centro_salud, nombre_vacuna, lote_vacuna) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                valores = (nombre,segundo_nombre, apellido,nro_dni,fecha_nacimiento,dosis,
                        fecha_aplicacion, centro_salud, nombre_vacuna, lote_vacuna)
                cursor.execute(sentencia,valores)
    except Exception as e:
        print(f'Ocurrió un error al cargar los datos: {e}')
    finally:
        cursor.close()
        return redirect(url_for('home'))
    
def borrar_paciente(id):
    try:
        with db:
            with db.cursor() as cursor:
                sentencia = f'DELETE FROM paciente WHERE id_paciente = {id}'
                cursor.execute(sentencia, id)
    except Exception as e:
        print(f'No se puedo borrar el paciente: {e}')
    finally:
        cursor.close()
        return redirect(url_for('home'))

def editar_paciente(id):
    nombre = request.form['nombre']
    segundo_nombre = request.form['segundo_nombre']
    apellido = request.form['apellido']
    nro_dni = request.form['nro_dni']
    fecha_nacimiento = request.form['fecha_nacimiento']
    dosis = request.form['dosis']
    centro_salud = request.form['centro_salud']
    
    try:
        with db:
            with db.cursor() as cursor:
                sentencia = 'UPDATE paciente SET nombre=%s, segundo_nombre = %s, apellido=%s,nro_dni=%s, fecha_nacimiento=%s, dosis=%s, centro_salud=%s WHERE id_paciente=%s'
                valores = (nombre, segundo_nombre, apellido,nro_dni,fecha_nacimiento,dosis,
                        centro_salud, id)
                cursor.execute(sentencia, valores)
    except Exception as e:
        print(f'No se pudo modificar los valores: {e}')
    finally:
        cursor.close()
        return redirect(url_for('home'))
    