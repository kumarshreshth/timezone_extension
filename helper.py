import requests

class Converter:
    __API_Key = "2afd2ab632e9434f91f37b7f66b69d6d"

    def timeConverter(self,current_location,current_datetime,queried_location):
        url = "https://timezone.abstractapi.com/v1/convert_time?api_key={key}&base_location={v1}&base_datetime={v2}&target_location={v3}".format(key=__class__.__API_Key,v1=current_location,v2=current_datetime,v3=queried_location)
        response = requests.get(url)
        try:
            data = response.json()
            current_location_time = data["base_location"]
            target_location_time = data["target_location"]
            print("Base_location : {location} , Time : {time}".format(location=current_location_time["datetime"],time=current_location_time["timezone_location"]))
            print("Target_location : {location} , Time : {time}".format(location=target_location_time["datetime"],time=target_location_time["timezone_location"]))

        except Exception as e:
            print("Error : ",e)
            