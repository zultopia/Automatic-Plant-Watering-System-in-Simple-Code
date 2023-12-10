def automatic_watering_system(switch, interval_time, soil_moisture_height):
    # Check switch state
    if switch == "ON":
        switch_state = 1
    else:
        switch_state = 0

    # Check interval time (every 3 days)
    interval_set = 3
    if interval_time % interval_set == 0:
        interval_state = 1
    else:
        interval_state = 0

    # Check soil moisture sensing
    height_limit = 5        # In cm
    if soil_moisture_height > height_limit:
        moisture_state = 1  # Moist soil
    else:
        moisture_state = 0  # Dry soil

    # Applying the logic circuit
    result = switch_state or (interval_state and not moisture_state)

    return result