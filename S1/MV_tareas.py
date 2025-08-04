from flask.views import MethodView
from flask import Flask, jsonify, request
import json
import os


app = Flask(__name__)
task_file = ("tareas.json")
valid_state = ("Por hacer", "En proceso", "Completada")


def read_tasks():
    if not os.path.exists(task_file):
        return []
    with open (task_file, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open (task_file, "w") as f:
        json.dump(tasks, f, indent=4)

class Crud_task(MethodView):
    
    def get_task():
        estado= request.args.get("estado")
        tasks = read_tasks()
        if estado:
            tasks = [t for t in tasks if t ["estado"]== estado]
        return jsonify(tasks)


    def create_task():
        new = request.get_json()
        tasks = read_tasks()
        if 'id' not in new or any(t['id'] == new['id'] for t in tasks):
                return jsonify({'error': 'ID duplicado o no proporcionado'}), 400

        for space in ['titulo', 'descripcion', 'estado']:
            if space not in new or not new[space]:
                return jsonify({'error': f'{space} es obligatorio'}), 400

        if new['estado'] not in valid_state:
            return jsonify({'error': 'Estado inválido'}), 400

        tasks.append(new)
        save_tasks(tasks)
        return jsonify(new), 201


    def edit_tasks(id):
        data= request.get_json()
        tasks= read_tasks()
        for task in tasks:
            if task ["id"]==id:
                task.update({k: v for k, v in data.items() if k in ['titulo', 'descripcion', 'estado']})
                if "estado" in data and data["estado"] not in valid_state:
                    return jsonify({"error": "Estado invalido"}), 400
                save_tasks(tasks)
                return jsonify(task)
        return jsonify({"Error":"Tarea no encontrada"}), 404


    def delete_tasks(id):
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
