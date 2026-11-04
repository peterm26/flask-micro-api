import requests

BASE_URL = "http://127.0.0.1:5000"

hello_response = requests.get(f"{BASE_URL}/hello")
print("GET /hello:", hello_response.status_code, hello_response.json())

data_response = requests.get(f"{BASE_URL}/data")
print("GET /data:", data_response.status_code, data_response.json())

post_response = requests.post(
    f"{BASE_URL}/data",
    json={"student": "Peter", "assignment": "Flask Micro-API"},
)
print("POST status:", post_response.status_code)
print("POST response:", repr(post_response.text))