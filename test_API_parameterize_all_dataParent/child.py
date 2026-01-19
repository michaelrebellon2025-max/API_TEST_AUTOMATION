import requests
import pytest

"""" 
I stack parametrize to run multiple user ids without duplicating the test code. 
the same logic can be applied to all the user ids for testing 1
"""
#PyTest evaluates parameter lists at import time.

def get_all_user_ids():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    return [user["id"] for user in response.json()]
@pytest.mark.parametrize("user_id", get_all_user_ids())
@pytest.mark.parametrize(
    "parent, child, child2, expected_type",
    [
        ("id","","",int),
        ("name","","",str),
        ("username","","",str),
        ("email", "","",str),
        ("address", "street","",str),
        ("address", "suite","",str),
        ("address", "city","",str),
        ("address", "zipcode","",str),
        ("address", "geo", "lat",str),
        ("address", "geo", "lng",str),
        ("phone","","",str),
        ("website","","",str),
        ("company","name","",str),
        ("company", "catchPhrase","",str),
        ("company", "bs","",str)

    ]
)
def test_check_nested_string(user_id, parent, child, child2, expected_type):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
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
            value=data[parent][child]
    else:
        value=data[parent]
    assert isinstance(value, expected_type), \
        f"{parent}->{child}->{child2} expected {expected_type}, got {type(value)}"

    if expected_type is str:
        assert value, f"{parent}->{child}->{child2} is empty"
