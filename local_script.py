import requests
import json

user_input = input("enter the countryCode:" "\n")


res = requests.get(url="https://www.travel-advisory.info/api")
if res.status_code == 200:
    # print(res.json())
    res_json = res.json()
else:
    raise Exception(f"Failed to connect with status code: {res.status_code}")


with open("data_json.json", "w") as f:
    f.write(json.dumps(res_json, indent=4))  # convert to json

with open("data_json.json") as f:
    new_data = json.load(f)
# print(new_data)

for i in new_data["data"]:
    if user_input.upper() in new_data["data"][i]["iso_alpha2"]:
        print(f"Country name is : {new_data['data'][user_input.upper()]['name']}")
        break
else:
    raise Exception(f"Country Code {user_input} not found")

# uvicorn app:app --reload
