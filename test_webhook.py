import requests

user_message = "Hi, How are you?."

request_message = {"message": user_message}

url = "http://localhost:5678/webhook-test/68873c99-cd38-4517-a917-138222d68714"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])


