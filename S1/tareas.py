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

def verify_state(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = request.get_json()
        if "estado" not in data or data["estado"] not in valid_state:
            return jsonify({"error": "Estado inválido"}), 400
        return func(*args, **kwargs)
    return wrapper
    
@app.route("/tareas", methods=["GET"])
def get_task():
    estado= request.args.get("estado")
    tasks = read_tasks()
    if estado:
        tasks = [t for t in tasks if t ["estado"]== estado]
    return jsonify(tasks)


@app.route("/tareas", methods=["POST"])
@verify_state
def create_task():
    new = request.get_json()
    tasks = read_tasks()
    for t in tasks:
        if new["id"]==t["id"]:
            return jsonify({'error': 'ID duplicado'}), 400
    for space in ["id","titulo", "descripcion", "estado"]:
        if space not in new or not new[space]:
            return jsonify({'error': f'{space} es obligatorio'}), 400
    tasks.append(new)
    save_tasks(tasks)
    return jsonify(new), 201


@app.route("/tareas/<int:id>", methods=["PUT"])
@verify_state
def edit_tasks(id):
    data= request.get_json()
    tasks= read_tasks()
    for task in tasks:
        if task ["id"]==id:
            task.update({k: v for k, v in data.items() if k in ['titulo', 'descripcion', 'estado']})
            
            save_tasks(tasks)
            return jsonify(task)
    return jsonify({"Error":"Tarea no encontrada"}), 404


@app.route("/tareas/<int:id>", methods=["DELETE"])
def delete_tasks(id):
    tasks = read_tasks()
    new_tasks = [t for t  in tasks if t["id"] != id]
    if len(tasks) == len(new_tasks):
        return jsonify({"Error": "No se encontro la tarea"}), 404
    save_tasks(new_tasks)
    return jsonify({"mensaje": "Tarea eliminada"}), 200


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
