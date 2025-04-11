# 🌡️ Smart Temp Logger

A simulated IoT temperature monitoring and control system using **Python** and **Google Sheets**.  
It mimics temperature readings, logs them into Google Sheets every few seconds, and updates fan status based on threshold (35°C).

![Terminal View](screeenshots/terminalview.png)  
*Simulated readings being logged in real-time.*

![Google Sheet View](screeenshots/sheetview.png)  
*Live Google Sheet logging and fan control updates.*

---

## 📌 Features

- ✅ Simulates random temperature values
- ✅ Logs timestamped temperature data to Google Sheets
- ✅ Turns "FAN ON" if temperature exceeds 35°C, else "FAN OFF"
- ✅ Simple Python threading to simulate real-time behavior
- ✅ No actual hardware required

---

## 🧰 Tech Stack

- **Python 3.x**
- `gspread` for Google Sheets API
- Google Service Account Credentials
- Google Sheets (Cloud-based storage)

---

## 🚀 How It Works

- Every few seconds, a random temperature is generated.
- This temperature and a timestamp are logged to the sheet.
- If the temperature is more than 35°C, the fan status is marked `ON`; else it's `OFF`.

---

## 📁 Folder Structure

```
smart-temp-logger/
│
├── simulated_temp_logger.py       # Main Python Script
├── creds.json                     # Google Service Account Credentials
├── screenshots/
│   ├── terminalview.png
│   └── sheetview.png
└── README.md                      # You're here!
```

---

## 🛠️ Setup & Usage

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/smart-temp-logger.git
cd smart-temp-logger
```

2. **Install Requirements**

```bash
pip install gspread oauth2client
```

3. **Add Google Sheets Credentials**

- Visit [Google Cloud Console](https://console.cloud.google.com/)
- Create a service account and enable the **Google Sheets API**
- Download the `creds.json` and place it in your project folder
- Share your target Google Sheet with the email in your `creds.json`

4. **Create Google Sheet**

- Name the sheet: `TemperatureControlSystem`
- Add these headers in row 1:
  ```
  Timestamp | Temperature | Fan Status
  ```

5. **Run the Simulation**

```bash
python simulated_temp_logger.py
```

---

## 🧪 Example Output

- `Timestamp`: 2025-04-11 14:25:12
- `Temperature`: 37.5°C
- `Fan Status`: ON

---


## 🙌 Credits

Made  by [Pratik Halnor]  
Inspired by smart automation using Python & IoT principles.
