from apis.nutritionix import Nutritionix
from datetime import datetime
from apis.sheety import Sheety
nutrition_api = Nutritionix()
sheety_api = Sheety()
user_data = {
    "gender": "male",
    "weight_kg": 90,
    "height_cm": 180,
    "age" : 25
}

time = datetime.now()
time_hours = f"{time.hour}:{time.minute}:{time.second}"
time = time.strftime("%Y-%m-%d")
data = nutrition_api.get_exercise_stats(input("Ce exercitii ai facut azi ?"), user_data)
print(data)
sheety_data = {
    "date" : time,
    "time" : time_hours,
    "exercise" : data["exercises"][0]["name"],
    "duration" : data["exercises"][0]["duration_min"],
    "calories" : data["exercises"][0]["nf_calories"]

}
sheety_api.add_row(sheety_data)