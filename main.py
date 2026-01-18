import requests

def test_get_user():
    url = "https://jsonplaceholder.typicode.com/users/8"
    response = requests.get(url)

    # 1. Status code check
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # 2. Parse JSON
    data = response.json()

    # 3. Check 'name'
    assert 'name' in data, "Name field missing"
    assert isinstance(data['name'], str) and data['name'], "Name is empty or not a string"

    # 4. Check 'email'
    assert 'email' in data, "Email field missing"
    assert "@" in data['email'] and data['email'], f"Invalid email: {data['email']}"

    # 5. Check 'phone'
    assert 'phone' in data, "Phone field missing"
    assert isinstance(data['phone'], str) and data['phone'], "Phone is empty or not a string"

    #6. Check 'address'
    assert 'address' in data, "Address field missing"
    assert "street" in data['address'] and data['address'], "Address is empty"
    assert isinstance(data['address']['street'],str)and data['address']['street'], "street is not str or empty"

    # Optional: check other nested fields
    assert 'city' in data['address'] and data['address']['city'], "City missing or empty"
    assert 'zipcode' in data['address'] and data['address']['zipcode'], "Zipcode missing or empty"

    #check 'company'
    assert 'company' in data, "Company field is missing"
    assert isinstance(data['company']['name'], str) and data['company']['name'], "Company is either empty or not a string"


import requests
import pytest

@pytest.mark.parametrize(
    "parent", "child", "child2"
    [
        ("id","",""),
        ("name","",""),
        ("username","",""),
        ("email", "",""),
        ("address", "street",""),
        ("address", "suite",""),
        ("address", "city",""),
        ("address", "zipcode",""),
        ("address", "geo", "lat"),
        ("address", "geo", "lng"),
        ("phone","",""),
        ("website","",""),
        ("company","name",""),
        ("company", "catchPhrase",""),
        ("company", "bs","")

    ]
)
def check_nested_string(parent, child, child2):
    url= "https://jsonplaceholder.typicode.com/users/8"
    response= requests.get(url)
    assert response.status_code ==200
    data = response.json()

    assert parent in data, f"{parent} missing"
    if child:
        assert child in data[parent], f'{child} missing in {parent}'
        if child2:
            assert child2 in data[parent][child], f'{child2} missing in {child}'
            value= data[parent][child][child2]
        else:
            value=date[parent][child]
    else:
        value=data[parent]
    assert isinstance(value,str) and value, f'{parent}->{child}->{child2} is empty or not a string'

