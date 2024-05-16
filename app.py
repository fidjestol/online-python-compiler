from flask import Flask, request, jsonify
import docker

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json['code']
    result = execute_python_code(code)
    return jsonify({"result": result})

def execute_python_code(code):
    client = docker.from_env()
    try:
        container = client.containers.run("python-runner", command=f"python -c '{code}'", remove=True, stdout=True, stderr=True)
        return container.decode()
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
