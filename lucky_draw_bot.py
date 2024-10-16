import pyautogui
import time

# Disable the FAILSAFE feature
pyautogui.FAILSAFE = False

def find_and_click_image(image_path):
    """
    Locate an image on the screen and click on it.
    
    :param image_path: Path to the image file
    :return: True if image found and clicked, False otherwise
    """
    try:
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.99995)  # Reduced sensitivity
        if button_location:
            # Divide coordinates by two
            button_x, button_y = button_location
            button_x /= 2
            button_y /= 2

            print(f"Image found, coordinates: ({button_x}, {button_y})")  # Print location info
            pyautogui.moveTo(button_x, button_y)  # Move mouse to new coordinates
            time.sleep(1)  # Add a delay before clicking
            pyautogui.click()  # Click
            print("Clicked!")
            time.sleep(1)  # Wait for 1 second
            return True
        else:
            print("Image not found.")
    except Exception as e:
        print(f"Error: {e}")
    return False

def scroll_screen():
    """Scroll the screen less."""
    pyautogui.scroll(-10)  # Reduced scroll amount

def click_empty_space():
    """Click slightly to the right of the center-left of the screen."""
    screen_width, screen_height = pyautogui.size()
    pyautogui.click(screen_width * 0.1, screen_height // 2)  # Click at a point slightly right of center-left

# Main loop
while True:
    # Find and click "Join the Draw" image
    if find_and_click_image('/Users/user_name/file_location/join_the_draw.png'):
        print("Join the Draw image found and clicked.")

        # Find and click "Join the Lucky Draw" image
        if find_and_click_image('/Users/user_name/file_location/join_the_lucky_draw.png'):
            print("Join the Lucky Draw image found and clicked.")
            click_empty_space()
            print("Clicked empty space.")
        else:
            print("Join the Lucky Draw not found, continuing to scroll.")
    else:
        print("Join the Draw not found, continuing to scroll.")

    # Scroll and try again
    scroll_screen()
    time.sleep(2)  # Wait for 2 seconds