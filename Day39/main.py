from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


dm = DataManager()
fd = FlightSearch()
notification = NotificationManager()
sheet_data = dm.read_row()
for data in sheet_data:
    if data["iataCode"] == "":
        destination_cod = fd.get_destinition_code(data["city"])
        dm.update_row(data["id"], destination_cod)

for data in sheet_data:
    flight_data = fd.get_lowest_price(data["iataCode"])
    if flight_data:
        current_price = float(flight_data["price"]["base"])
        current_date = flight_data["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        return_date = flight_data["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")[0]
        if current_price < data["lowestPrice"]:
            notification.send_sms(
                price=current_price,
                from_city="LON",
                to_city=data["city"],
                out_date= current_date,
                return_date = return_date
            )



