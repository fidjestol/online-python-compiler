from locust import HttpUser, task, between
import json

class PythonCodeExecutionUser(HttpUser):
    wait_time = between(1, 2)  # Simulated users will wait 1-2 seconds between tasks

    @task
    def submit_code(self):
        # Sample Python code to execute
        code = "print('Hello, World')"
        headers = {'content-type': 'application/json'}
        payload = json.dumps({"code": code})
        
        # POST request to the `/run` endpoint
        self.client.post("/run", data=payload, headers=headers)

    @task(1)
    def index(self):
        # Users will also occasionally fetch the index page
        self.client.get("/")
