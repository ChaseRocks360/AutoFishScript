import time
from PIL import ImageGrab
import pyautogui
import keyboard
import os

# Function to capture the specific pixel color
def get_pixel_color(x, y):
    screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    return screenshot.getpixel((0, 0))

# Main loop
target_color = (255, 85, 85)  # RGB value for #FF5555
x, y = 1601, 919

while True:
    if keyboard.is_pressed('F7'):  # Check if F7 is pressed to stop the script
        print("F7 pressed. Exiting script.")
        os._exit(1)  # Exit the script

    # Get the color of the specific pixel
    pixel_color = get_pixel_color(x, y)

    if pixel_color == target_color:
        # First right-click
        pyautogui.click(button='right')
        print("Target color detected at (1601, 919). First right-click performed, waiting 5 milliseconds before the next click...")

        # Wait 5 milliseconds
        time.sleep(0.005)

        # Second right-click
        pyautogui.click(button='right')
        print("Second right-click performed, waiting 500 milliseconds before resuming detection...")

        # Wait 500 milliseconds after the second right-click
        time.sleep(0.5)

    # Check the pixel color every 5 milliseconds
    time.sleep(0.005)
