from flask import Flask, request, jsonify
import docker
from docker.errors import ContainerError, APIError
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
        container = client.containers.run("python-runner", command="python -c 'import os; exec(os.environ[\"PYTHON_CODE\"])'", detach=True, remove=False, stdout=True, stderr=True, network_disabled=True, mem_limit='128m', environment={'PYTHON_CODE': code})
        result = container.wait(timeout=10)
        if result['StatusCode'] == 0:
            # If execution finished without errors, get the output
            return container.logs().decode('utf-8')
        else:
            # Handle various cases or error codes here
            return "Execution did not complete within the allowed time or ended with errors."
    except ContainerError as e:
        return f"Error occurred while executing code: {str(e)}"
    except APIError as e:
        return f"Docker API error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    finally:
        try:
            # Cleanup: Ensure the container is removed if still present
            container.remove(force=True)
        except Exception:
            pass  # Handle exceptions in cleanup if necessary

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)