import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import time
from datetime import datetime

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open("TemperatureControlSystem").sheet1

# Function to log temp and status
def log_temperature(temp):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fan_status = "FAN ON" if temp > 35 else "FAN OFF"
    sheet.append_row([timestamp, temp, fan_status])
    print(f"📡 Logged | Temp: {temp}°C | Status: {fan_status}")

# Main loop: generate 35 values over 2 minutes (1 every ~3.5 sec)
for _ in range(35):
    simulated_temp = random.randint(25, 45)
    log_temperature(simulated_temp)
    time.sleep(3.5)  # ~2 mins total for 35 readings
