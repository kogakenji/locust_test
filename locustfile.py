from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled""" # noqa E501
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post("/login", {"username": "kenji", "password": "password"}) # noqa E501

    def logout(self):
        self.client.post("/logout")

    @task(1)
    def index(self):
        self.client.get("/")

    # @task(1)
    # def profile(self):
    #     self.client.get("/profile")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
