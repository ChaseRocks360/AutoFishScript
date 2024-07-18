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
def contains_target_color(image, target_color=(231, 84, 73)):
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            if pixels[x, y][:3] == target_color:  # Compare only RGB values
                return True
    return False

# Initialize variables
last_checked = time.time()

# Main loop
while True:
    if keyboard.is_pressed('F7'):  # Check if F7 is pressed to stop the script
        print("F7 pressed. Exiting script.")
        os._exit(1)  # Exit the script

    image = capture_screen()

    if contains_target_color(image):
        # Right-click
        pyautogui.click(button='right')
        print("First right-click detected, waiting before the next click...")
        # Wait 1 second after right-clicking to avoid multiple triggers
        time.sleep(1)
        
        # Right-click again
        pyautogui.click(button='right')
        print("Second right-click detected, resuming detection...")

        # Wait 1 second after second right-click to avoid multiple triggers
        time.sleep(1)

    # Check the screen every second
    while time.time() - last_checked < 1:
        if keyboard.is_pressed('F7'):  # Check again if F7 is pressed while waiting
            print("F7 pressed. Exiting script.")
            os._exit(1)  # Exit the script
        time.sleep(0.01)
    last_checked = time.time()
