from flask_sqlalchemy import SQLAlchemy                     # V1 ARCHIVOS BASE PARA EL ARCHIVO EN DONDE LLAMAMOS AL SQLALCHEMY
db = SQLAlchemy()                                           # V1 Y DEFINIMOS QUE HAREMOS UN DB QUE SE COMUNICARÁ CON SQLALCHEMY Y RETORNARA TODA LA INFORMACION QUE TIENE

class Contact(db.Model):                                                    # V3 ----------> 
    __tablename__ = 'contacts'                                              # V3    COMENZAMOS LA CREACION DE LA TABLA
    id = db.Column(db.Integer, primary_key=True)                            # V3        COLUMNA 1
    name = db.Column(db.String(100), nullable=False)                        # V3        COLUMNA 2
    phone = db.Column(db.String(100), nullable=False)                       # V3        COLUMNA 3

    def serialize(self):                                                    # V3    AQUI TOMAMOS LA INFORMACION PARA SERIALIZARLA. ESTO SIGNIFICA QUE LOS DATOS LOS TRANSFORMARA 
        return {                                                            # V3    EN UN OBJETO. EN ESTE CASO SELF FUNCIONA COMO EL THIS EN JS/REACT, Y POR LO TANTO LA INFORMACION
            "id": self.id,                                                  # V3    QUEDA DINAMICA.
            "name": self.name,                                              # V3            OJO Y FIJARSE DE QUE DESPUES DEL RETURNO SE VE CLARAMENTE UN OBJETO!!! {ATR1, ATR2, ATR3,..., ATRN}
            "phone": self.phone                                             # V3            <----------
        }