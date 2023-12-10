def automatic_watering_system(switch, interval_time, soil_moisture_height):
    # Check switch state
    if switch == "ON":
        switch_state = 1
    else:
        switch_state = 0

    # Check interval time (every 3 days)
    if interval_time % 3 == 0:
        interval_state = 1
    else:
        interval_state = 0

    # Check soil moisture sensing
    if soil_moisture_height > 5:
        moisture_state = 1  # Moist soil
    else:
        moisture_state = 0  # Dry soil

    # Applying the logic circuit
    result = switch_state or (interval_state and not moisture_state)

    return result

def main():
    print("🌿 Welcome to Azul's Smart Garden! 🌿")

    print("Hello, Azul. How was your day? Ready to watering your plants?")

    # User input
    switch_input = input("Enter switch state (ON/OFF): ")
    interval_time_input = int(input("Enter interval time (in days): "))
    soil_moisture_height_input = float(input("Enter soil moisture height (in cm): "))

    # Checking the automatic watering system status
    status = automatic_watering_system(switch_input, interval_time_input, soil_moisture_height_input)

    # Displaying the result
    if status:
        print("Automatic Plant Watering System is ON. Your plants are getting some love! 💧🌱")
    else:
        print("Automatic Plant Watering System is OFF. Your garden is taking a break. 😴")

if __name__ == "__main__":
    main()