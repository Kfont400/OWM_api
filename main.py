import smtplib
import requests
from twilio.rest import Client
import os


class Weather:
    def __init__(self) -> None:
        self.weather_params = {
            "appid": os.environ.get("OWM_Api_Key"),
            "lat": 29.7604,
            "lon": -95.3698,
            "cnt": 3,
        }
        self.OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

    def checkWeather(self):
        response = requests.get(self.OMW_Endpoint, params=self.weather_params)
        return response.json()


class Alert:
    alert_me = True

    def __init__(self):
        self.account_sid = os.environ.get("twilio_sid")
        self.auth_token = os.environ.get("twilio_auth_token")
        self.client = Client(self.account_sid, self.auth_token)
        self.my_email = "kfont400@gmail.com"
        self.password = os.getenv("password")
        self.rain = "It's gonna rain today ☔️"

    def sendMessage(self, response):
        for i in range(3):
            weather_condition = response["list"][i]["weather"][0]["id"]
            if weather_condition < 700:
                alert_me = True

            # if alert_me == True:
            #     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            #         connection.starttls()
            #         connection.login(user=self.my_email, password=self.password)
            #         connection.sendmail(
            #             from_addr=self.my_email,
            #             to_addrs=self.my_email,
            #             msg=f"Subject:Be Prepared\n\n{self.rain}",
            #         )
            message = self.client.messages.create(
                from_="+18447524823", body="It's gonna rain today ☔️", to="+18777804236"
            )
        return message.status


weather = Weather()
alert = Alert()

print(alert.sendMessage(weather.checkWeather()))
