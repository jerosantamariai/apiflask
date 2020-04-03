from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Contact(db.Model):                                    # V3 ----------> 
    __tablename__ = 'contacts'                              # V3    
    id = db.Column(db.Integer, primary_key=True)            # V3
    name = db.Column(db.String(100), nullable=False)        # V3
    phone = db.Column(db.String(100), nullable=False)       # V3

    def serialize(self):                                    # V3
        return {                                            # V3
            "id": self.id,                                  # V3
            "name": self.name,                              # V3
            "phone": self.phone                             # V3            <----------
        }