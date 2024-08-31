import tkinter as tk
import time
import pyautogui
import threading

def open_cmd_and_run_commands():
    for _ in range(3):
        # Press Win+R to open the Run dialog
        pyautogui.hotkey('win', 'r')
        
        # Wait for the Run dialog to open
        time.sleep(0.3)
        
        # Type 'cmd' to open Command Prompt
        pyautogui.write('cmd')
        
        # Press Enter to execute the command
        pyautogui.press('enter')
        
        # Wait for the Command Prompt to open
        time.sleep(0.7)
        
        # Set text color and run 'dir /s'
        pyautogui.write('color a')
        time.sleep(0.3)
        pyautogui.press('enter')
        
        # Wait for the color change to apply
        time.sleep(0.5)
        
        pyautogui.write('dir /s')
        pyautogui.press('enter')
        
        # Wait for a short moment before opening the next Command Prompt
        time.sleep(1)

def prank():
    # Create the main window
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Make the window full screen
    root.attributes('-topmost', False)  # Do not keep the window on top

    # Create a label with the prank message
    label = tk.Label(root, text="GET PRANKED!!!!", font=('Helvetica', 48), fg='green')
    label.pack(expand=True)

    # Prevent the window from being closed with Alt+F4
    def disable_event():
        pass

    root.protocol("WM_DELETE_WINDOW", disable_event)

    # Update the window to show it
    root.update()

    time.sleep(35)

    root.destroy()

# Run the prank in a separate thread
prank_thread = threading.Thread(target=prank)
prank_thread.start()

# Ensure the prank screen has enough time to open
time.sleep(1)

# Open Command Prompt and execute commands three times
open_cmd_and_run_commands()
