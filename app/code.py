import requests

map = {0:"cats",1:"dogs"}

def predict(model,img):
    url = "http://172.17.0.2/api/genhog"
    
    response = requests.get(url, json={"img" : img})
    if response.status_code == 200:
        try:
            resData = response.json()
            resDataList = [resData[i] for i in resData]
            animal = model.predict(resDataList)
            result = map.get(animal[0])
            
            return result
        except requests.exceptions.JSONDecodeError as e:
            print("Json Error : ",e)
    else:
        print("API Error : ",response.status_code)
