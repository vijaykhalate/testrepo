import random

import pytest
import requests




post_url = "https://gorest.co.in/public/v2/users"
get_url = "https://gorest.co.in/public/v2/users"
put_url = "https://gorest.co.in/public/v2/users"
delete_url = "https://gorest.co.in/public/v2/users"

bearer_token = "8a94fe3b4e42fdecfe114dacd9edf23949ca31eda3d487ce97147dd326a9d45e"

header_values = {"Authorization" : f"Bearer {bearer_token}",
                  "Content-Type": "application/json" }


@pytest.fixture(scope='module')
def create_user():
    random_number = random.randint(1, 3000)
    email = f"vijay_{random_number}@gmail.com"
    data = {
        "id": 108,
        "name": "vijay",
        "email": email,
        "gender": "male",
        "status": "inactive"
    }
    response = requests.post(post_url, json = data, headers=header_values)
    print(response.content)
    response_data = response.json()
    id =  response_data.get("id")

    return id,email

def test_post_api_unauthorised_request():
    global newid
    random_number = random.randint(1,3000)
    data = {
        "id": 108,
        "name": "vijay",
        "email": f"vijay_{random_number}@gmail.com",
        "gender": "male",
        "status": "inactive"
    }

    response = requests.post(post_url, headers=None, json=data)
    print(response.content)
    response_data = response.json()
    assert response.status_code == 401, f"Expected Status Code 401, but we got {response.status_code}"
    assert response_data["message"] == "Authentication failed", f"This is not expected message"

def test_post_api_success_request():
    global newid
    random_number = random.randint(1, 3000)
    print("_______________________")
    print(random_number)
    print("_______________________")
    data = {
        "id": 108,
        "name": "vijay",
        "email": f"vijay_{random_number}@gmail.com",
        "gender": "male",
        "status": "inactive"
    }
    response = requests.post(post_url, json = data, headers=header_values)
    print(response.content)
    response_data = response.json()
    newid =  response_data.get("id")
    print("________________________")
    print(newid)
    print("_________________________")
    assert response.status_code == 201 , f"Exepcted Status Code is 201 but we got {response.status_code}"
    assert newid is not None, f"Recived newid as None"
    assert response_data["id"] == newid, f"Expected newid "
    assert response_data["name"] == data["name"], f"Expected 'name' to be {data['name']}, but we recived {response_data['name']}"
    assert response_data["email"] == data["email"], f"Expected 'email' to be {data['email']}, but we recived {response_data['email']}"
    assert response_data["gender"] == data["gender"], f"Expected 'gender' to be {data['gender']}, but we recived {response_data['gender']}"
    assert response_data["status"] == data["status"], f"Expected 'status' to be {data['status']}, but we recived {response_data['status']}"

    delete_full_url = f"{delete_url}/{newid}"
    response = requests.delete(delete_full_url, headers=header_values)
    print(response)
    assert response.status_code == 204, f"Expected Status Code is 201 but we got {response.status_code}"

def test_post_api_unprocessable_entity_request():
    data = {}
    response =requests.post(post_url, headers=header_values, json=data)
    print(response.content)
    response_data = response.json()
    assert response.status_code == 422, f"Expected 422 status code but we got {response.status_code}"

def test_get_api_request(create_user):
    # global newid
    id,email = create_user
    full_url = f"{get_url}/{id}"
    print(full_url)
    response = requests.get(full_url, headers= header_values)
    print(full_url)
    print(response.content)
    assert response.status_code == 200, f"Expecting 200 status code but got {response.status_code}"

    delete_full_url = f"{delete_url}/{id}"
    print(delete_full_url)
    response = requests.delete(delete_full_url, headers=header_values)
    print(response.content)
    assert response.status_code == 204, f"Expecting 204 status code but got {response.status_code}"

def test_update_put_request(create_user):
    id1, email2 = create_user
    print("id--------------------------------------------------",id1)
    print("email-----------------------------------------------",email2)
    put_full_url = f"{put_url}/{id1}"
    print("-----------------------------------------------------------",put_full_url)
    random_number = random.randint(1, 3000)
    email3 = f"vijay_{random_number}@gmail.com"
    data = {
        "name": "vijay",
        "email": email3,
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(put_full_url, headers=header_values, json=data)
    print(response.content)
    assert  response.status_code == 200, f"Expecting status code 200 but got {response.status_code}"

    delete_full_url = f"{delete_url}/{id1}"
    print("____________________________________________",delete_full_url)
    response = requests.delete(delete_full_url, headers=header_values)
    print("Deleted---------------",response.status_code)
    assert response.status_code == 204, f"Expecting 200 status code but got {response.status_code}"

def test_delete_request(create_user):
    id,email = create_user
    delete_full_url = f"{delete_url}/{id}"
    print("This is full delete api url ----------", delete_full_url)
    response = requests.delete(delete_full_url, headers=header_values)
    print(response.content)
    assert response.status_code == 204, f"Expecting 204 status code but got {response.status_code}"