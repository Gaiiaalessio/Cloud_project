from locust import HttpUser, task
from requests.auth import HTTPBasicAuth
import requests
import random

with open("output.txt", "a") as f:
    f.write(f"_________________________________________________\n")


class NextcloudUser(HttpUser):
    host = "http://localhost:8080"
    auth = None
    users_list = list(range(1, 31))

    def on_start(self):
        random.shuffle(self.users_list)
        i = self.users_list.pop()
        self.user = 'user' + '{:d}'.format(i)
        self.password = 'abc123abc!'
        self.auth = HTTPBasicAuth(self.user, self.password)
        self.verify_authentication()


    def verify_authentication(self):
        response = self.client.head("/remote.php/dav", auth=self.auth)
        if response.status_code != 200:
            with open("output.txt", "a") as f:
                f.write(f"Authentication failed for user {self.user}: {response.text}.\n")
            raise Exception(f"Authentication failed for user {self.user}")


    @task
    def propfind(self):
        try:
            response = self.client.request("PROPFIND", "/remote.php/dav", auth=self.auth)
            response.raise_for_status()
        except Exception as e:
            with open("output.txt", "a") as f:
                f.write(f"Error during PROPFIND request: {e} for user {self.user}.\n")


    @task
    def upload_file(self):
        filename = "large.txt"
        with open( filename, 'rb') as f:
            response = self.client.put("/remote.php/dav/files/" + self.user + "/" + filename,
                                       auth=self.auth, data=f, name="/remote.php/dav/files/[user]/large.txt")
        if response.status_code not in [201, 204]:
            with open("output.txt", "a") as f:
                f.write(f"Error during PUT request: {response.status_code} for user {self.user}.\n")
            return

        for i in range(0, 5):
            self.client.get("/remote.php/dav/files/" + self.user + "/" + filename,
                            auth=self.auth, name="/remote.php/dav/files/[user]/large.txt")

        self.client.delete("/remote.php/dav/files/" + self.user + "/" + filename,
                           auth=self.auth, name="/remote.php/dav/files/[user]/large.txt")
