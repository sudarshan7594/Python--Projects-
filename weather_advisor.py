# Smart Weather Advisor
# Created by Sudarshan Kushwaha

print("=" * 40)
print("       SMART WEATHER ADVISOR")
print("=" * 40)

name = input("Enter your name: ")

try:
    temp = float(input("Enter today's temperature (°C): "))
    humidity = float(input("Enter humidity (%): "))

    if not -50 <= temp <= 60 or not 0 <= humidity <= 100:
        print("Please enter valid weather values.")

    else:
        print("\nHello,", name)
        print("\n--- WEATHER REPORT ---")
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")

        if temp >= 35:
            print("Weather: Very Hot")
            print("Advice: Drink plenty of water.")

        elif temp >= 25:
            print("Weather: Warm")
            print("Advice: Wear light cotton clothes.")

        elif temp >= 15:
            print("Weather: Pleasant")
            print("Advice: Enjoy your day!")

        else:
            print("Weather: Cold")
            print("Advice: Wear warm clothes.")

        if humidity >= 80:
            print("Humidity: Very High")
            print("Suggestion: Carry an umbrella.")

        elif humidity >= 50:
            print("Humidity: Moderate")
        else:
            print("Humidity: Low")

        print("\nStay Safe and Enjoy Your Day!")
        print("Developed by Sudarshan Kushwaha")

except ValueError:
    print("Invalid input! Please enter numbers.")

print("=" * 40)