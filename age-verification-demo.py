import requests
import json

while(1):
    val = input("Please enter a birthdate (YYYY-MM-DD): ")
    r = requests.get('https://api.maurer.gg/verify_age/' + val)
    if(r.status_code == 200):
        data = r.json()
        if(data['verified']):
            print("User is over 13.")
        else:
            print("User is not over 13.")
    else:
        print("The server returned error Status Code" + r.status_code)    
    