import requests
import json
from ApiJanuaryProject import auto_lijst

URL = "https://system-service-mathieudj.cloud.okteto.net/auto/{aantal}"
URL1 = "https://system-service-mathieudj.cloud.okteto.net/auto/kleur/${color}"
URL2 = "https://system-service-mathieudj.cloud.okteto.net/auto/horsepower/{min_horsepower}/{max_horsepower}"
URL3 = "https://system-service-mathieudj.cloud.okteto.net/auto/{merk}"
URL4 = "https://system-service-mathieudj.cloud.okteto.net/auto/{merk}/{model}"
URL5 = "https://system-service-mathieudj.cloud.okteto.net/users/"
URL6 = "https://system-service-mathieudj.cloud.okteto.net/token"

def test_geef_auto():
    # Test that the endpoint returns a list of cars with the specified number of elements
    response = requests.get(URL.format(aantal=3))
    assert response.status_code == 200
    assert len(response.json()) == 3

    # Test that the endpoint returns an error message when a negative number is passed as a parameter
    response = requests.get(URL.format(aantal=-1))
    assert response.status_code == 200
    assert response.json() == {"foutmelding": "Het aantal auto's moet een positief getal zijn."}

def test_geef_auto():
    # Test that the endpoint returns a list of cars
    response = requests.get('https://system-service-mathieudj.cloud.okteto.net/auto/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_geef_auto_kleur():
    # Test that the endpoint returns a list of cars with the specified color
    response = requests.get(URL1.format(color="rood"))
    assert response.status_code == 200
    assert all(car["kleur"] == "rood" for car in response.json())

    # Test that the endpoint returns an empty list when no cars with the specified color are found
    response = requests.get(URL1.format(color="roos"))
    assert response.status_code == 200
    assert response.json() == []


def test_geef_auto_horsepower():
    # Test that the endpoint returns a list of cars with horsepower within the specified range
    response = requests.get(URL2.format(min_horsepower=200, max_horsepower=300))
    assert response.status_code == 200
    for car in response.json():
        assert 200 <= car["horsepower"] <= 300

    # Test that the endpoint returns an empty list if no cars have horsepower within the specified range
    response = requests.get(URL2.format(min_horsepower=1000, max_horsepower=2000))
    assert response.status_code == 200
    assert response.json() == []

def test_read_users():

    headers = {'Authorization': 'Bearer "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoZWxsbzVAZ21haWwuY29tIiwiZXhwIjoxNjczMTIzMzM2fQ.nckz2xd0BUmX-Li4_6YksOPRfAOgLOHGR-E6kc_eUXc'}
    response = requests.get("https://system-service-mathieudj.cloud.okteto.net/users/", headers=headers)

    assert response.status_code == 200


def test_read_user_id():
    # Test that the endpoint returns a user with the specified ID
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoZWxsbzVAZ21haWwuY29tIiwiZXhwIjoxNjczMTIzMzM2fQ.nckz2xd0BUmX-Li4_6YksOPRfAOgLOHGR-E6kc_eUXc"}
    response = requests.get("https://system-service-mathieudj.cloud.okteto.net/users/1", headers=headers)
    assert response.status_code == 200

    # Test that the endpoint returns a 404 error when an invalid user ID is passed as a parameter
    response = requests.get("https://system-service-mathieudj.cloud.okteto.net/users/999", headers=headers)
    assert response.status_code == 404

def test_voeg_auto_toe():
    # Test that the endpoint returns a success message when a valid request is made
    response = requests.post("https://system-service-mathieudj.cloud.okteto.net/auto/", json={"merk": "Ford", "model": "Fiesta", "kleur": "blauw", "horsepower": 150})
    assert response.status_code == 200
    assert response.json() == {"message": "Auto toegevoegd aan lijst"}

def test_verwijder_auto():
    # Test that the endpoint returns a success message when a valid request is made
    response = requests.delete(URL3.format(merk="Mazda"))
    assert response.status_code == 200
    assert response.json() == {"message": "Auto's met merk Mazda verwijderd"}

def test_update_auto():

    response = requests.put(URL4.format(merk="Non-existent brand", model="Non-existent model"), json={"horsepower": 200})
    assert response.status_code == 200
    assert response.json() == {"status": "not found"}

def test_create_user():
    # Test that the endpoint returns a 400 error when an invalid request is made
    response = requests.post(URL5, json={"email": "newuser@example.com", "password": "password"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}


def test_login_for_access_token():
    # Test that the endpoint returns a JWT when a valid request is made
    response = requests.post(
        URL6,
        json={"username": "user@example.com", "password": "password"}
    )
    assert response.status_code == 422
    assert "detail" in response.json()












