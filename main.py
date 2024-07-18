import time
from PIL import ImageGrab
import pyautogui
import keyboard
import os

# Function to capture the screen
def capture_screen():
    screenshot = ImageGrab.grab()
    return screenshot

# Function to check for the specific colors
def contains_target_color(image, target_colors):
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            if pixels[x, y][:3] in target_colors:  # Compare only RGB values
                return True
    return False

# Main loop
target_colors = [(231, 84, 73), (255, 85, 85)]  # RGB values for #E75449 and #FF5555
while True:
    if keyboard.is_pressed('F7'):  # Check if F7 is pressed to stop the script
        print("F7 pressed. Exiting script.")
        os._exit(1)  # Exit the script

    image = capture_screen()

    if contains_target_color(image, target_colors):
        # First right-click
        pyautogui.click(button='right')
        print("First right-click detected, waiting 5 milliseconds before the next click...")

        # Wait 5 milliseconds
        time.sleep(0.005)

        # Second right-click
        pyautogui.click(button='right')
        print("Second right-click detected, waiting 500 milliseconds before resuming detection...")

        # Wait 500 milliseconds after the second right-click
        time.sleep(0.5)

    # Check the screen every 5 milliseconds
    time.sleep(0.005)
