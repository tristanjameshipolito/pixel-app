import cv2
import numpy as np
import pyautogui
import time
import random

# Function to detect the target image and click its half coordinates
def detect_and_click(image, label):
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > 0.9:
        x, y = max_loc[0] + image.shape[1] // 2, max_loc[1] + image.shape[0] // 2  # Get center coordinates
        #print(f"{label} button found at x={x} and y={y}")
        half_x, half_y = x // 2, y // 2
        #print(f"Clicking at half coordinates: x={half_x} and y={half_y}")
        pyautogui.doubleClick(x=half_x, y=half_y)  # Click at half coordinates
        #time.sleep(5)  # Wait for 5 seconds
        # Move the mouse away randomly within the specified range
        #moveaway_x = random.randint(1068, 1075)
        #moveaway_y = random.randint(600, 615)
        #pyautogui.moveTo(x=moveaway_x, y=moveaway_y, duration=1.5)
        return True, x, y
    else:
        #print(f"{label} button not found")
        return False, None, None
        

# Load the target images
create_button_img = cv2.imread('img/create_button.png')
collect_button_img = cv2.imread('img/collect_button.png')

# Main loop
while True:
    # Detect and click the "create" button
    create_found, create_x, create_y = detect_and_click(create_button_img, "Create")
    # Detect and click the "collect" button
    collect_found, collect_x, collect_y = detect_and_click(collect_button_img, "Collect")

    time.sleep(1)  # Wait for 5 seconds before checking again
