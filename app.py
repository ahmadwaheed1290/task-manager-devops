from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
next_id = 1

@app.route('/')
def home():
    return jsonify({'message': 'Task Manager API is running'})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    global next_id
    data = request.get_json()
    task = {
        'id': next_id,
        'title': data.get('title'),
        'completed': False
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    