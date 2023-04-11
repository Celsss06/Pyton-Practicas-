import mysql.connector

try:
  conex=mysql.connector.connect(host='loclhost',
                                 user='root',
                                 passwd='',
                                 database='registro_alumnos')
except Exception as err:
    print (' ERROR AL CONECTARSE')
else:
    print ('CONEXION EXITOSA')
try:
    #se insertan los dcatos que se quieren poner en la tabla 
    Cur1= conex.cursor()
    insertar= "insert into alumnos values (Renata Jacquelin, 'Celis Pacheco', '04220012', 'ISIC', '2')"
    Cur1.execute (insertar)
    conex.commit()
except Exception as err:
    print ('ERROR ENCONTRADO', err)
else:
    print ('REGISTRO EXCITOSO')
#se cierra la conexion a la base de datos
conexion.close()