app_name = "passengers"
app_title = "Passengers"
app_publisher = "Your Name"
app_description = "Extract and store passenger data from Bahrain CPR identity card"
app_email = "your@email.com"
app_license = "MIT"

doc_events = {
    "Passenger": {
        "validate": "passengers.passengers.doctype.passenger.passenger.extract_data_from_cpr"
    }
}
