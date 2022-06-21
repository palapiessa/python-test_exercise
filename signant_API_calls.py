import requests

def register_user(data):
    url = "http://localhost:8080/api/users"
    headers = {
        'content-type': "application/json"
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code

def retrieve_users(auth_header):
    url = "http://localhost:8080/api/users"
    response = requests.get(url, headers=auth_header)
    return response.json()

def retrieve_user_info(user_id, auth_header):
    url = "http://localhost:8080/api/users/{user}".format(user=user_id)
    response = requests.get(url, headers=auth_header)
    return response.json()

def update_user_info(user_id, auth_header, data):
    url = "http://localhost:8080/api/users/{user}".format(user=user_id)
    response = requests.put(url, headers=auth_header, json=data)