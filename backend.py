import requests


API_KEY = '3ba9d8a4c7da374b3b6b0cbf685c62dc'
def get_data(place, forecast_days, kind):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    place = "Tokyo"
    days = 5
    option = "Temperature"
    data = get_data(place, days, option)
    print(data)  # For testing purposes, print the data to the console