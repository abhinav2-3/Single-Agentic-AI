import requests

response = requests.get("https://api.github.com")
# print(response)
print(response.status_code)
# print("Response JSON : ", response.json())
# print("Current user url : ", response.json()["current_user_url"])

user = {"name": "Abhinav", "work": "Software Engineer", "age": "22"}

print(f"My API is {response.json()["current_user_url"]} with {response.status_code}")

print("User : ", type(user))
print("User : ", user["name"])
print("User : ", user.get("age"))
