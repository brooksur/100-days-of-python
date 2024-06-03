import requests
import datetime as dt
import smtplib
import time

COORDINATES = (40.758701, -111.876183)
SUNRISE_SUNSET_URL = 'https://api.sunrise-sunset.org/json'
ISS_NOW_URL = "http://api.open-notify.org/iss-now.json"
MY_EMAIL = 'test@test.test'
MY_PASSWORD = 'abc123'


def is_dark():
    parameters = {
        'lat': COORDINATES[0],
        'lng': COORDINATES[1],
        'formatted': 0
    }

    response = requests.get(url=SUNRISE_SUNSET_URL, params=parameters)
    response_data = response.json()

    sunrise = response_data['results']['sunrise']
    sunset = response_data['results']['sunset']

    sunrise_hour = int(sunrise.split('T')[1].split(':')[0])
    sunset_hour = int(sunset.split('T')[1].split(':')[0])

    print(sunrise_hour, sunset_hour)
    time_now = dt.datetime.now().hour

    return time_now >= sunset_hour or time_now <= sunrise_hour


def add_sub_5(num):
    return [num - 5, num + 5]


def iss_is_near():
    response = requests.get(url=ISS_NOW_URL)
    response.raise_for_status()
    data = response.json()

    iss_lat_range = add_sub_5(float(data["iss_position"]["latitude"]))
    iss_lng_range = add_sub_5(float(data["iss_position"]["longitude"]))

    my_lat = COORDINATES[0]
    my_lng = COORDINATES[1]

    near_lat = iss_lat_range[0] <= my_lat <= iss_lat_range[1]
    near_lng = iss_lng_range[0] <= my_lng <= iss_lng_range[1]

    return near_lat and near_lng


def main():
    if is_dark() and iss_is_near():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg='Subject:Look up!\n\nThe ISS is above you in the sky'
        )

# Run main every sixty seconds
while True:
    time.sleep(60)
    main()
