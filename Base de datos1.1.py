import sqlite3
# Nos conectamos a la base de datos (si no existe la crea)
conexion = sqlite3.connect("PRUEBA.db")
# Crear una tabla
conexion.execute("""create table alumnos1( id integer primary key AUTOINCREMENT,nombre varchar,edad integer)""")
conexion.close()
conexion = sqlite3.connect("PRUEBA.db")
# Insertamos alumnos
conexion.execute("Insert into alumnos(nombre,edad,matricula)", ("Renata", 18,))
conexion.execute("Insert into alumnos(nombre,edad, matricula)", ("Hugo", 19))
conexion.execute("Insert into alumnos(nombre,edad, matricula)", ("Alondra", 18))
conexion.execute("Insert into alumnos(nombre,edad, matricula)", ("Aaron", 19))

conexion.commit()

# se imprime uno
alumno = conexion.execute("select * from alumnos where nombre = 'Renata'")
# Esto es para solamente traer el primero o bien para traer uno
fil = alumno.fetchone()
#imprimimos la fila (el alumno)
print(fil)
# Cerramos la conexión con SQLITE
conexion.close()