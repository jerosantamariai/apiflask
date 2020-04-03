from flask import Flask, jsonify, request, render_template      # V1 JSONIFY DEVUELVE EN FORMATO JSON LA INFO, REQUEST PERMITE SABER POR CUAL METODO (GET, PUT, POST O DELETE) ESTOY EJECUTANDO LA PETICION Y RENDER... ME PERMITE GENERAR UNA SALIDA EN CODIGO HTML DEL ARCHIVO QUE SE LE INDIQUE
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS                                     # V1 HASTA AQUI IMPORTO LA INFORMACION DE LAS LIBRERIAS QUE INSTALE ANTERIORMENTE
from models import db                                           # V1 ESTO LO IMPORTO UNA VEZ QUE SE CREA EL ARCHIVO MODELS.PY CON SUS COMANDOS RESPECTIVOS


app = Flask(__name__)                                           # V1 INSTANCIA DE FLASK, QUE RECIBE UN ATRIBUTO DE PYTHON QU ES __NAME__ QUE ES OBLIGATORIO. 
app.url_map.strict_slashes = False                                                  # V2 CON ESTE CODIGO EVITAMOS QUE SEA MUY ESTRICTA LA APLICACION A LA HORA DE QUE BUSQUE O LEA LAS RUTAS POR CONTENER O NO SLASHES (/) EXPLICACION MIN [13:30 - 14:00]
app.config['DEBUG'] = True                                      # V1 ME PERMITE VER LOS ERRORES DE MI APLICACION
app.config['ENV'] = 'development'                               # V1 ESTE ES EL ENTORNO EN DONDE VOY A PUBLICAR MI APLICACION//EN PROCESO DE DESARROLLO PONEMOS 'development', DE LO CONTRARIO 'production' PARA PUBLICAR EN NUESTRO SERVIDO WEB
app.config['SQLALCHEMY_DATABASE_URI'] = ''                      # V1 ESTA Y LA SIGUIENTE CONFIGURACION LLAMAN A LA LIBRERIA DE SQLALCHEMY, ESTE ME VA A INDICAR EN QUE GESTOR DE BASE DE DATOS VOY A TRABAJAR
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False            # V1 HACE UN TRACKING DE LO QUE MODIFICO DAAAAH!

Migrate(app, db)                                                # V1 TRAMOS MIGRATE QUE LE DAMOS LOS PARAMETROS DONDE TRABAJARA, Y QUE SEREA LA APP Y LA BD
CORS(app)                                                       # V1 TRAMOS A FUNCIONAMIENTO CORS PARA LA APP

manager = Manager(app)                                          # V1 TRAEMOS A FUNCIONAR MANAGER
manager.add_command("db", MigrateCommand)                       # V1 ESTO ME GENERA LA POSIBILIDAD DE HACER 3 COSAS: 1. init (solo la primera vez o por que borre la carpeta de migraciones), 2. migrate (crea las migraciones) y 3. upgrade (se encarga de enviar las migraciones a la BBDD)

@app.route("/")                                                 # V1 CREA UNA NUEVA RUTA A TRAVEZ DE @APP.ROUTE (QUE ES LA DIRECTIVA DE FLASK QUE PERMITE DEFINIR RUTAS). RECIBE COMO PARAMETRO OBLIGATORIO EL NOMBRE QUE QUIERO DARLE A LA RUTA (EN ESTE CASO SE MANTUVO COMO "/"), Y PUEDE RECIBIR UN PARAMETRO OPCIONAL (SE OMITE YA QUE POR DEFECTO ES "GET") UN ARRAY QUE SON LOS METODOS POR LOS QUE PERMITO AL USUARIO LLEGAR A LA RUTA. ESTO SE ESCRIBIRIA POR EJEMPLO COMO: @app.route("/", methods=['GET'])
def root():                                                     # V1 SE DEFINE LA FUNCION POR LA CUAL SE ASOCIA Y LLEGA A LA RUTA DE LA LINEA ANTERIOR
    return render_template('index.html')                        # V1 Y POR LO TANTO ME LLEVA A NUESTRO ARCHIVO HTML

@app.route('/api/test', methods=['GET', 'POST'])                                    # V2 
@app.route('/api/test/<int:id>', methods=['GET', 'PUT', 'DELETE'])                  # V2
def test(id = None):                                                                # V2 DEFINIMOS UNA FUNCION DE PYTHON EN DONDE LE DAMOS UN PARAMETRO ID. ESTE PARAMETRO LO DEJAMOS EN NONE YA QUE HAY METODOS QUE NO LO REQUIEREN MIENTRAS QUE OTROS SI LO REQUIEREN.
    if request.method == 'GET':                                                     # V2 ----------> 
        return jsonify({"msg": "method GET"}), 200                                  # V2    PARA CADA METODO SE APLICA UN IF QUE UTILIZARA EL REQUEST DE FLASK PARA CAPTURAR EL METODO QUE SE ESTA SOLICITANDO 
    if request.method == 'POST':                                                    # V2    ESTE DEVOLVERA EN FORMATO JSON UN OBJETO CON EL MENSAJE DEL METODO JUNTO CON SU INFORMACION DE ESTADO DE PETICION (EDP) DESEADO.
        return jsonify({"msg": "method POST"}), 200                                 # V2
    if request.method == 'PUT':                                                     # V2    EN RESUMEN:
        return jsonify({"msg": "method PUT"}), 200                                  # V2        IF REQUEST.METHOD == "METODO"
    if request.method == 'DELETE':                                                  # V2            RETURN JSONIFY(OBJETO), EDP
        return jsonify({"msg": "method DELETE"}), 200                               # V2              <----------

@app.route('/api/test/<int:id>/category/<int:cat_id>', methods=['GET', 'POST'])
def test2(id, cat_id):
    if request.method == 'GET':
        return jsonify({"valores": {"id": id, "cat_id": cat_id}}), 200
    if request.method == 'POST':
        return jsonify({"valores": {"id": id, "cat_id": cat_id}}), 200

if __name__ == '__main__':                                      # EJECUTAMOS LA APLICACION
    manager.run()                                               # EJECUTAMOS LA APLICACION A TRAVEZ DE MANAGER... CUANDO REALIZAMOS LA CONFIGURACION DEL FLASK Y TRAEMOS A FUNCIONAMIENTO TODAS LAS LIBRERIAS YA PODEMOS DARLE AL TERMINAL ++ python app.py runserver ++ Y NUESTRA APLICACION YA SE PODRA VER EN EL ARCHIVO HTML DADA LA RUTA ENTREGADA EN @APP.ROUTE