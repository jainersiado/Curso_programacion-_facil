import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Jd992502,",
    database = "american_rider"
)

#cursor = recorre las filas y acciona las bases de datos
cursor = conexion.cursor()

cursor.execute("CREATE TABLE clientes"
                "(id INT NOT NULL AUTO_INCREMENT,"
                "nombre VARCHAR (32) NOT NULL," 
                "apellidos VARCHAR (64) NOT NULL," 
                "telefono VARCHAR (9) NOT NULL," 
                "direccion VARCHAR (256)," 
                "PRIMARY KEY (id));")


#tipos de datos
#varchar = almacena strings
#int = alamcena valores enteros
#float = almacena valoeres decimales

#create database x
#drop database