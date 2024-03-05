from timezone_extension.helper import Converter
from datetime import datetime
import pytz


current_location ="America/New_York"
print(current_location)
target_location = "Europe/Paris"
print(target_location)
current_time = datetime.now(pytz.timezone(current_location)).strftime("%Y-%m-%d %H:%M:%S")
print(current_time)

request = Converter()
request.timeConverter(current_location,current_time,target_location)
