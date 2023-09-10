import requests


base_url = "https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=51.50&lon=0.12&appid=d0d3d6886441c441428e3394999980a6"

def get_temperature(dt_txt):
    try:
        response = requests.get(base_url)
        data = response.json()
        for forecast in data["list"]:
            if forecast["dt_txt"] == dt_txt:
                temperature = forecast["main"]["temp"]
                return f"Temperature at {dt_txt}: {temperature}°C"
        return "Data not found for the specified date and time."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_wind_speed(dt_txt):
    try:
        response = requests.get(base_url)
        data = response.json()
        for forecast in data["list"]:
            if forecast["dt_txt"] == dt_txt:
                wind_speed = forecast["wind"]["speed"]
                return f"Wind Speed at {dt_txt}: {wind_speed} m/s"
        return "Data not found for the specified date and time."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_pressure(dt_txt):
    try:
        response = requests.get(base_url)
        data = response.json()
        for forecast in data["list"]:
            if forecast["dt_txt"] == dt_txt:
                pressure = forecast["main"]["pressure"]
                return f"Pressure at {dt_txt}: {pressure} hPa"
        return "Data not found for the specified date and time."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    while True:
        print("\nOptions:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            print(get_temperature(date_time))
        elif choice == "2":
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            print(get_wind_speed(date_time))
        elif choice == "3":
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            print(get_pressure(date_time))
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
