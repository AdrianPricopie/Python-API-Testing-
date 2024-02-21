import requests


def get_status():
    return requests.get("https://simple-books-api.glitch.me/status")


# .json() ne returneaza body-ul raspunsului requestului facut
# print(get_status().json())
# .status_code ne returneaza status code-ul requestului trimis
# print(get_status().status_code)


