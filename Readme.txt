You have to download these libraries for the code to run
infi.systray
threading
schedule
plyer

Python script that uses the requests library to make an API call to a website that
provides prayer timings (azan) for a specific city and country. The response from 
the API is parsed to extract the times for different prayers (Fajr, Sunrise, Dhuhr, Asr, Maghrib, Isha)
and these times are then used to update the hover text of a system tray icon, which is created using the 
infi.systray library.

This script is written in Python and uses the "requests" library to make an API request to
"http://api.aladhan.com/v1/timingsByCity" to get prayer timings for the city of Ancona in Italy.
then uses the "infi.systray" library to create a system tray icon that displays the prayer timings.
The "schedule" library is used to periodically update the data every 1 hour. It also uses "plyer" library
to send notifications . It checks for internet connectivity using "urllib" library before making the API 
request and uses "datetime" library to get the current time. The script also uses "threading" library to 
handle the shutdown process of system tray icon.