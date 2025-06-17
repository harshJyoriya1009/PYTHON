import pyautogui
import pyperclip
import time

# Give you some time to move mouse away or prepare screen
time.sleep(2)

# Step 1: Click the icon
pyautogui.click(1206, 1040)
time.sleep(1)  # wait for the app to open or respond

# Step 2: Click and drag to select text
pyautogui.moveTo(671, 221)
pyautogui.mouseDown()
pyautogui.moveTo(1829, 959, duration=0.5)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy to clipboard (Ctrl+C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Get the clipboard content
copied_text = pyperclip.paste()
print("Copied Text:", copied_text)
