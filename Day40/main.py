from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt

dm = DataManager()
fd = FlightSearch()
notification = NotificationManager()
sheet_data = dm.read_row()
customers = dm.customer_info()
for data in sheet_data:
    if data["iataCode"] == "":
        destination_cod = fd.get_destinition_code(data["city"])
        dm.update_row(data["id"], destination_cod)

date_today= dt.datetime.now() + dt.timedelta(days=1)
date_after_six_months = dt.datetime.now() + dt.timedelta(days=180)
for data in sheet_data:
    flight_data = fd.check_flights(origin_city_code="LON", destination_city_code= data["iataCode"], from_time= date_today.strftime("%Y-%m-%d"), to_time=date_after_six_months.strftime("%Y-%m-%d"))
    if not flight_data:
        continue
    current_price = float(flight_data["price"])
    current_date = flight_data["departure"].split("T")[0]
    return_date = flight_data["return_date"].split("T")[0]
    if current_price < data["lowestPrice"]:
        for customer in customers:
            notification.send_mail(
                email_to_send=customer["email"],
                price=current_price,
                from_city="LON",
                to_city=data["city"],
                stops=flight_data["stops"],
                out_date=current_date,
                return_date=return_date
            )




