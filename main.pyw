import requests
import json
from infi.systray import SysTrayIcon
import threading
import schedule
import time

def update_data():
    # Check for internet connectivity
    try:
        requests.get('http://google.com', timeout=5)
    except requests.ConnectionError:
        print("No internet connection available.")
        exit()

    # Make the API request
    try:
        response_API = requests.get('http://api.aladhan.com/v1/timingsByCity?city=Ancona&country=Italy&method=3')
        response_API.raise_for_status()
        data = response_API.json()
        timings = data.get('data', {}).get('timings', {})
        if not timings:
            raise ValueError("Timings data not found in API response.")
        prayer_time_Fajr = timings.get('Fajr')
        prayer_time_Sunrise = timings.get('Sunrise')
        prayer_time_Dhuhr = timings.get('Dhuhr')
        prayer_time_Asr = timings.get('Asr')
        prayer_time_Maghrib = timings.get('Maghrib')
        prayer_time_Isha = timings.get('Isha')
        if not all([prayer_time_Fajr, prayer_time_Sunrise, prayer_time_Dhuhr, prayer_time_Asr, prayer_time_Maghrib, prayer_time_Isha]):
            raise ValueError("One or more prayer timings not found in API response.")
        """
        print(prayer_time_Fajr)
        print(prayer_time_Sunrise)
        print(prayer_time_Dhuhr)
        print(prayer_time_Asr)
        print(prayer_time_Maghrib)
        print(prayer_time_Isha)
        """
        hover_text = "Fajr:"+prayer_time_Fajr+" Sunrise:"+prayer_time_Sunrise+" Dhuhr:"+prayer_time_Dhuhr+" Asr:"+prayer_time_Asr+" Maghrib:"+prayer_time_Maghrib+" Isha:"+prayer_time_Isha
        sysTrayIcon.update("mosque.ico", hover_text)
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
        exit()
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        exit()
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        exit()
    except requests.exceptions.RequestException as err:
        print ("Something went wrong:",err)
        exit()
    except ValueError as e:
        print(str(e))
        exit()

def on_quit_callback(systray):
    threading.Thread(target=systray.shutdown).start()
hover_text = "Loading..."
sysTrayIcon = SysTrayIcon("mosque.ico", hover_text, on_quit=on_quit_callback, default_menu_index=1)
sysTrayIcon.start()
schedule.every(1).hours.do(update_data)
update_data()
while True:
    schedule.run_pending()
    time.sleep(1)