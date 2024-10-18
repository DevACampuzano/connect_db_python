#pip install mysql-connector
#pip install python-dotenv
import mysql.connector # type: ignore
from dotenv import load_dotenv # type: ignore
import os
#Cargar variables de entorno
load_dotenv()

#Clase para conectar a la base de datos
class ConnetorDB:

    #Constructor
    def __init__(self):
        dbUser= os.getenv("DB_USER")
        dbPassword= os.getenv("DB_PASSWORD")
        dbHost= os.getenv("DB_HOST")
        dbName= os.getenv("DB_NAME")
        self.db =mysql.connector.connect(user=dbUser, password=dbPassword, host=dbHost, database= dbName )
        self.cur = self.db.cursor()

    #Metodo para consultar los usuarios
    def consultaUsuarios(self):
        self.cur.execute("SELECT * FROM usuarios where estado = 1")
        rows = self.cur.fetchall()
        return rows
    
    #Metodo para registrar un usuario
    def registrarUsuario(self, nombre, email, edad):
        sql = "INSERT INTO usuarios (nombre, email, edad) VALUES (%s, %s, %s)"
        val = (nombre, email, edad)
        self.cur.execute(sql, val)
        self.db.commit()
    
    #Metodo para imprimir la lista de usuarios
    def imprimiListaUsuarios(self, rows):
        if len(rows)==0:
            print("No se encontraron registros")
            return
        
        for row in rows:
            print("-----------------Datos del usuario-----------------")
            print("Id: ",row[0])
            print("Nombre: ",row[1])
            print("Email: ",row[2])
            print("Edad: ",row[3])
            print("Estado: ",row[4])
    
    #Metodo para consultar un usuario por ID
    def consultaUsuarioID(self, id):
        sql = f"SELECT * FROM usuarios where id = {str(id)} and estado = 1"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows
    
    #Metodo para actualizar un usuario
    def actualizarUsuarios(self, id, nombre=None, email=None, edad=None):
        sql = "UPDATE usuarios SET "

        if nombre != None:
            sql = sql +f" nombre = '{nombre}'"

        if email != None:
            sql = sql + f" email = '{email}'"

        if edad != None:
            sql = sql + f" edad = {edad}"
        
        sql = sql+ f" WHERE id = {id}"

        self.cur.execute(sql)
        self.db.commit()
    
    #Metodo para eliminar un usuario
    def eliminarUsuario(self, id):
        sql = f"UPDATE usuarios SET estado = 0 WHERE id = {id}"
        self.cur.execute(sql)
        self.db.commit()


if __name__ == "__main__":
    #Instancia de la clase
    cDB = ConnetorDB()

    #cDB.registrarUsuario("Juan", "juan@test.co", 25)
    #user= cDB.consultaUsuarioID(3)
    #cDB.eliminarUsuario(1)

    list =cDB.consultaUsuarios()
    cDB.imprimiListaUsuarios(list)
    cDB.db.close()
