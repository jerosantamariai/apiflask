from flask import Flask, jsonify, request, render_template     # JSONIFY DEVUELVE EN FORMATO JSON LA INFO, REQUEST PERMITE SABER POR CUAL METODO (GET, PUT, POST O DELETE) ESTOY EJECUTANDO LA PETICION Y RENDER... ME PERMITE GENERAR UNA SALIDA EN CODIGO HTML DEL ARCHIVO QUE SE LE INDIQUE
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS                                    # HASTA AQUI IMPORTO LA INFORMACION DE LAS LIBRERIAS QUE INSTALE ANTERIORMENTE
from models import db                                          # ESTO LO IMPORTO UNA VEZ QUE SE CREA EL ARCHIVO MODELS.PY CON SUS COMANDOS RESPECTIVOS


app = Flask(__name__)                                          # INSTANCIA DE FLASK, QUE RECIBE UN ATRIBUTO DE PYTHON QU ES __NAME__ QUE ES OBLIGATORIO. 
app.config['DEBUG'] = True                                     # ME PERMITE VER LOS ERRORES DE MI APLICACION
app.config['ENV'] = 'development'                              # ESTE ES EL ENTORNO EN DONDE VOY A PUBLICAR MI APLICACION//EN PROCESO DE DESARROLLO PONEMOS 'development', DE LO CONTRARIO 'production' PARA PUBLICAR EN NUESTRO SERVIDO WEB
app.config['SQLALCHEMY_DATABASE_URI'] = ''                     # ESTA Y LA SIGUIENTE CONFIGURACION LLAMAN A LA LIBRERIA DE SQLALCHEMY, ESTE ME VA A INDICAR EN QUE GESTOR DE BASE DE DATOS VOY A TRABAJAR
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False           # HACE UN TRACKING DE LO QUE MODIFICO DAAAAH!

Migrate(app, db)                                               # TRAMOS MIGRATE QUE LE DAMOS LOS PARAMETROS DONDE TRABAJARA, Y QUE SEREA LA APP Y LA BD
CORS(app)                                                      # TRAMOS A FUNCIONAMIENTO CORS PARA LA APP

manager = Manager(app)                                         # TRAEMOS A FUNCIONAR MANAGER
manager.add_command("db", MigrateCommand)                      # ESTO ME GENERA LA POSIBILIDAD DE HACER 3 COSAS: 1. init (solo la primera vez o por que borre la carpeta de migraciones), 2. migrate (crea las migraciones) y 3. upgrade (se encarga de enviar las migraciones a la BBDD)

@app.route("/")                                                # CREA UNA NUEVA RUTA A TRAVEZ DE @APP.ROUTE (QUE ES LA DIRECTIVA DE FLASK QUE PERMITE DEFINIR RUTAS). RECIBE COMO PARAMETRO OBLIGATORIO EL NOMBRE QUE QUIERO DARLE A LA RUTA (EN ESTE CASO SE MANTUVO COMO "/"), Y PUEDE RECIBIR UN PARAMETRO OPCIONAL (SE OMITE YA QUE POR DEFECTO ES "GET") UN ARRAY QUE SON LOS METODOS POR LOS QUE PERMITO AL USUARIO LLEGAR A LA RUTA. ESTO SE ESCRIBIRIA POR EJEMPLO COMO: @app.route("/", methods=['GET'])
def root():                                                    #SE DEFINE LA FUNCION POR LA CUAL SE ASOCIA Y LLEGA A LA RUTA DE LA LINEA ANTERIOR
    return render_template('index.html')                       #Y POR LO TANTO ME LLEVA A NUESTRO ARCHIVO HTML

if __name__ == '__main__':                                     # EJECUTAMOS LA APLICACION
    manager.run()                                              # EJECUTAMOS LA APLICACION A TRAVEZ DE MANAGER... CUANDO REALIZAMOS LA CONFIGURACION DEL FLASK Y TRAEMOS A FUNCIONAMIENTO TODAS LAS LIBRERIAS YA PODEMOS DARLE AL TERMINAL ++ python app.py runserver ++ Y NUESTRA APLICACION YA SE PODRA VER EN EL ARCHIVO HTML DADA LA RUTA ENTREGADA EN @APP.ROUTE