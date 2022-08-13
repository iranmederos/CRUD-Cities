from flask import Flask ,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)
CORS(app)
# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/flaskmysql'
#                                               user:clave@localhost/nombreBaseDatos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
ma=Marshmallow(app)
# defino la tabla
class Ciudad(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    imagen=db.Column(db.String(200))
    descripcion=db.Column(db.String(200))
    def __init__(self,nombre,imagen,descripcion):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.imagen=imagen
        self.descripcion=descripcion
 
db.create_all()  # crea las tablas
#  ************************************************************
class CiudadesSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','imagen','descripcion')
ciudad_schema=CiudadesSchema()            # para crear un producto
ciudades_schema=CiudadesSchema(many=True)  # multiples registros
 
 
# crea los endpoint o rutas (json)
@app.route('/ciudades',methods=['GET'])
def get_Ciudades():
    all_ciudades=Ciudad.query.all()     # query.all() lo hereda de db.Model
    result=ciudades_schema.dump(all_ciudades)  # .dump() lo hereda de ma.schema
    return jsonify(result)
 
 
@app.route('/ciudades/<id>',methods=['GET'])
def get_ciudad(id):
    ciudad=Ciudad.query.get(id)
    return ciudad_schema.jsonify(ciudad)

 
@app.route('/ciudades/<id>',methods=['DELETE'])
def delete_producto(id):
    ciudad=Ciudad.query.get(id)
    db.session.delete(ciudad)
    db.session.commit()
    return ciudad_schema.jsonify(ciudad)

@app.route('/ciudades', methods=['POST']) # crea ruta o endpoint
def create_producto():
    print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    imagen=request.json['imagen']
    descripcion=request.json['descripcion']
    new_ciudad=Ciudad(nombre,imagen,descripcion)
    db.session.add(new_ciudad)
    db.session.commit()
    return ciudad_schema.jsonify(new_ciudad)

@app.route('/ciudades/<id>' ,methods=['PUT'])
def update_producto(id):
    ciudad=Ciudad.query.get(id)
   
    nombre=request.json['nombre']
    imagen=request.json['imagen']
    descripcion=request.json['stock']
 
    ciudad.nombre=nombre
    ciudad.imagen=imagen
    ciudad.descripcion=descripcion
    db.session.commit()
    return ciudad_schema.jsonify(ciudad)

 
# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)  