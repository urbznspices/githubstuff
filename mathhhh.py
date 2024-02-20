
import math


def calculate_diameter():
    # Get user inputs
    velocity = float(input("Enter the velocity (m/s): "))
    density = float(input("Enter the air density (kg/m^3): "))
    drag_force = float(input("Enter the drag force (N): "))

    # Calculate the diameter
    diameter = math.sqrt((8 * drag_force) / (math.pi * density * velocity**2))

    # Print the result
    print("The diameter is:", diameter)


# Call the function
calculate_diameter()
