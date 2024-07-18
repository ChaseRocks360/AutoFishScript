import time
from PIL import ImageGrab
import pyautogui
import keyboard
import os

# Function to capture the screen
def capture_screen():
    screenshot = ImageGrab.grab()
    return screenshot

# Function to check for the specific color
def contains_color(image, target_color):
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            if pixels[x, y][:3] == target_color:  # Compare only RGB values
                return True
    return False

# Main loop
color1 = (255, 85, 85)  # RGB value for #FF5555
color2 = (63, 21, 21)   # RGB value for #3F1515

while True:
    if keyboard.is_pressed('F7'):  # Check if F7 is pressed to stop the script
        print("F7 pressed. Exiting script.")
        os._exit(1)  # Exit the script

    image = capture_screen()

    # Check for both colors
    color1_found = contains_color(image, color1)
    color2_found = contains_color(image, color2)

    if color1_found and color2_found:
        # First right-click
        pyautogui.click(button='right')
        print("Both colors detected. First right-click performed, waiting 5 milliseconds before the next click...")

        # Wait 5 milliseconds
        time.sleep(0.005)

        # Second right-click
        pyautogui.click(button='right')
        print("Second right-click performed, waiting 500 milliseconds before resuming detection...")

        # Wait 500 milliseconds after the second right-click
        time.sleep(0.5)

    # Check the screen every 5 milliseconds
    time.sleep(0.005)
