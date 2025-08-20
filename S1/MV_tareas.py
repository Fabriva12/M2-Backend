from flask.views import MethodView
from flask import Flask, jsonify, request
import json
import os
from functools import wraps


app = Flask(__name__)
task_file = ("tareas.json")
valid_state = ("Por hacer", "En proceso", "Completada")


class JSONReadError(Exception):
    pass
class JSONWriteError(Exception):
    pass

def read_tasks():
    try:
        if not os.path.exists(task_file):
            return []
        with open (task_file, "r") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise JSONReadError({"error":"El archivo no contiene un JSON válido"})
    except Exception as e:
        raise JSONReadError({"error":"Ocurrio un error inesperado"})

def save_tasks(tasks):
    try:
        with open (task_file, "w") as f:
            json.dump(tasks, f, indent=4)
    except TypeError as e:
        raise JSONWriteError({"error":"Los datos no son serializables a json"})

@app.errorhandler(JSONReadError)
def handle_json_read_error(error):
    return jsonify({"error": str(error)}), 500

@app.errorhandler(JSONWriteError)
def handle_json_write_error(error):
    return jsonify({"error": str(error)}), 500

def verify_spaces(data, id_require= True):
    mandatory_space = ["id","titulo", "descripcion", "estado"] if id_require else ["titulo", "descripcion", "estado"]
    for space in mandatory_space:
        if space not in data or not str(data[space]).strip():
            return False, f"El campo '{space}' es obligatorio"
    if data.get("estado") not in valid_state:
        return False, "Estado inválido"
    return True, None

class Crud_task(MethodView):
    
    def get():
        estado= request.args.get("estado")
        tasks = read_tasks()
        if estado:
            tasks = [t for t in tasks if t ["estado"]== estado]
        return jsonify(tasks)


    def post():
        data = request.get_json()
        valid_data, error_mg = verify_spaces(data, id_require=True)
        if not valid_data:
            return jsonify({"error": error_mg}), 400
        tasks = read_tasks()
        for t in tasks:
            if data["id"]==t["id"]:
                return jsonify({"error": "ID duplicado"}), 400
        tasks.append(data)
        save_tasks(tasks)
        return jsonify(data), 201


    def put(id):
        data= request.get_json()
        valid_data, error_mg = verify_spaces(data, id_require=False)
        if not valid_data:
            return jsonify({"error": error_mg}), 400
        tasks= read_tasks()
        for task in tasks:
            if task ["id"]==id:
                task.update(data)
                save_tasks(tasks)
                return jsonify(task)
        return jsonify({"Error":"Tarea no encontrada"}), 404


    def delete(id):
        tasks = read_tasks()
        new_tasks = [t for t  in tasks if t["id"] != id]
        if len(tasks) == len(new_tasks):
            return jsonify({"Error": "No se encontro la tarea"}), 404
        save_tasks(new_tasks)
        return jsonify({"mensaje": "Tarea eliminada"}), 200

app.add_url_rule("/tareas", methods=["GET"])
app.add_url_rule("/tareas/<int:id>", methods=["DELETE"])
app.add_url_rule("/tareas/<int:id>", methods=["PUT"])
app.add_url_rule("/tareas", methods=["POST"])


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
