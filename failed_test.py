import os
import pyautogui

# Wait for 2 seconds
pyautogui.sleep(2)

# Open the Run dialog
pyautogui.hotkey('win', 'r')

# Wait for 0.5 seconds
pyautogui.sleep(0.5)

# Type the command
pyautogui.typewrite('cmd')

# Press Enter
pyautogui.press('enter')

# Wait for 2 seconds
pyautogui.sleep(2)

# Type the AWS SES command
message = "Subject={Data='Failed Awareness Test'},Body={Text={Data='The user of the computer %username%'}}"
pyautogui.typewrite(f'aws ses send-email --from senderemail@gmail.com --destination ToAddresses=recieveremail@gmail.com --message "{message}"')

# Press Enter
pyautogui.press('enter')

# Wait for 0.5 seconds
pyautogui.sleep(0.5)

# Press the Down arrow key to close the Command Prompt window
pyautogui.press('down')
