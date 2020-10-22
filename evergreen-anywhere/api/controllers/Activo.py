from flask import jsonify, request
import json 
from baseDatos.db import cnx



class activo():
    global cur 
    cur = cnx.cursor()

    
    def list():
        
        lista = []
        cur.execute("SELECT * FROM activo")
        rows = cur.fetchall()
        print(rows)
        columns = [i[0] for i in cur.description]
        for row in rows:
            # Create a zip object from two lists
            registro = zip(columns, row)
            # Create a dictionary from zip object
            json = dict(registro)
            lista.append(json)
        cnx.close
        return jsonify(lista)
    def find(id):
        
        activo = cur.execute( "SELECT * FROM activo where id = '" + id + "'")
        cnx.close
        return jsonify(cur.fetchone())
    def create(body):
        
        sql = "INSERT INTO activo( nombre, cantidad, tipo, fecha_adquisicion, valor_compra, depreciacion_anual, precio_final) VALUES ( %(nombre)s, %(cantidad)s, %(tipo)s, %(fecha_adquisicion)s, %(valor_compra)s,  %(depreciacion_anual)s,  %(precio_final)s)"
        cur.execute(sql,body)        
        cnx.commit()

        return {'info': "Activo creado exitosamente"}, 200


    def delete(id):
        
        cur.execute("DELETE FROM activo where id = %(id)s", {'id' : id});
        cnx.commit()
        cnx.close
        return {'info': "activo eliminado"}, 200 
        

