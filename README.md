# 🔄 Load Testing Using Locust

This guide shows how to perform basic HTTP load testing using the **Locust** tool.

---

## ✅ Prerequisites

- Python 3.7 or higher installed
- Internet access to test target URLs

---

## 🛠️ Step 1: Install Locust

Open your terminal or command prompt and run:

```
pip install locust
```

## 📁 Step 2: Project Setup

1. Create a project folder named locust:

```
mkdir locust
cd locust
```
2. Inside the folder, create a file named locustfile.py and paste the following code:

```
from locust import HttpUser, task, between

class MyUser(HttpUser):

    wait_time = between(1, 3)

    @task
    def home_page(self):

        self.client.get("https://www.google.com/")

```
## 🚀 Step 3: Run Locust

Run the following command to start the Locust web interface:

```
python -m locust

```

🌐 Step 4: Access the Web Interface
Open your browser and go to:
http://localhost:8089/

- You will see the Locust web interface where you can:
- Set the number of users to simulate
- Define the spawn rate (users per second)
- Start the test and monitor performance metrics in real-time

```

```
