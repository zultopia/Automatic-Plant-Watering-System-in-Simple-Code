# Automatic-Plant-Watering-System-in-Simple-Code

This repository contains a project undertaken by me, Marzuli Suhada M (13522070), to fulfill the assignment for the IF2120 Discrete Mathematics paper in 2023. The source code consists of one stage: determining whether the automatic plant watering system is on or off based on the current conditions.

## Determining Factors

The system's operation is influenced by three factors:

1. <span style="color: #FF5733">**Switch On/Off**</span>
   - The variable `x` mirrors the manual switch's functionality. If `x` is active (1), the system is in an ON state, and the watering mechanism is engaged. If `x` is inactive (0), the system is in an OFF state, and the watering process is halted.

2. <span style="color: #33FF4E">**Interval Time Setting**</span>
   - The variable `y` represents an adjustable interval time setting. An active state (1) for `y` indicates that the system is within the specified time interval, allowing for flexible watering schedules. When `y` is inactive (0), the system responds to soil conditions immediately.

3. <span style="color: #339FFF">**Soil Moisture Sensing**</span>
   - The variable `z` reflects the conditions of soil moisture in a binary state: 1 (ON) for moist soil and 0 (OFF) for dry soil.

## Boolean Algebra Function

The final result is determined using the Boolean algebra function derived from minimization:
\[ f(x, y, z) = x + yz' \]

If the output is <span style="color: #33FF4E; font-weight: bold">1</span>, the automatic plant watering system will be ON, and the plants will be watered. Conversely, if the output is <span style="color: #FF5733; font-weight: bold">0</span>, the automatic plant watering system will be in a dormant state.

## How to Use

1. Input the current conditions:
   - Switch state (ON/OFF)
   - Interval time (in days)
   - Soil moisture height (in cm)

2. Run the program to check whether the automatic plant watering system is ON or OFF based on the given conditions.

Feel free to explore the source code and modify it for your needs!

<span style="font-size: larger; color: #FFC300; font-weight: bold">Happy Coding! 🌿💧</span>