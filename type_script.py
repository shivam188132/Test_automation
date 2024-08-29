import type_script
import time

# Give yourself a few seconds to click on the window where you want to type the code
time.sleep(5)

# Define the code as a string with proper syntax
code = '''
import pyautogui
import time

# Give yourself a few seconds to click on the window where you want to type the code
time.sleep(5)

# Define the code as a string with proper syntax
code = \"\"\"  # Your code goes here
import pyautogui
import time

time.sleep(2)
pyautogui.write('Hello, World!', interval=0.1)
\"\"\"

# Type the code
pyautogui.write(code, interval=0.05)
'''

# Type the code
type_script.write(code, interval=0.05)
