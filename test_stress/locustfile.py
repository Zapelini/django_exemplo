from locust import HttpLocust, TaskSet, task


def login(l):
    l.client.post("/login", {"username": "ellen_key", "password": "education"})


def index(l):
    l.client.get("/")


def profile(l):
    l.client.get("/profile")


class DjangoTasks(TaskSet):
    # tasks = {index:2, profile:1}
    tasks = [index]

    def on_start(self):
        # login(self)
        pass
    
    @task(1)
    def ping(self):
        self.client.get("/ping")


class WebsiteUser(HttpLocust):
    task_set = DjangoTasks
    min_wait=2000
    max_wait=9000
