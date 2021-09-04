import requests
from time import sleep
from pyromises import Promise


def fetch_data():
    response = requests.get("https://api.github.com/users/Nxrth-x")
    return response.json()


def sleep_for_a_while():
    sleep(1)
    print("Done sleeping")


Promise(sleep_for_a_while)

Promise(fetch_data).then(print)

print("Hello, world!")
