# Import the required classes from the locust module
from locust import HttpUser, task, between

# Define a user class that simulates a single user behavior
class MyUser(HttpUser):
    # Specify wait time between tasks: user will wait between 1 and 3 seconds before next action
    wait_time = between(1, 3)

    # Define a task (simulated action) for the user
    @task
    def home_page(self):
        # Simulate a GET request to the specified URL (Google homepage in this case)
        self.client.get("https://www.google.com/")