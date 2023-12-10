from system import automatic_watering_system

def main():
    print("🌿 Welcome to Azul's Smart Garden! 🌿")

    print("Hello, Azul. How was your day? Ready to watering your plants?")

    # User input
    x = input("Enter switch state (ON/OFF): ")
    y = int(input("Enter interval time (in days): "))
    z = float(input("Enter soil moisture height (in cm): "))

    # Checking the automatic watering system status
    status = automatic_watering_system(x, y, z)

    # Displaying the result
    if status:
        print("Automatic Plant Watering System is ON. Your plants are getting some love! 💧🌱")
    else:
        print("Automatic Plant Watering System is OFF. Your garden is taking a break. 😴")

if __name__ == "__main__":
    main()