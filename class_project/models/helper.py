"""Alta3 Research | BCopeland
    Stores any miscellaneous function for the application"""

import os
import sys
import time

def display_404():
    """Displays 404 if user inputs invalid menu path"""
    os.system('clear')
    print("404: Page Not Found")

def close_app():
    """Closes the application when called"""
    os.system('clear')
    print("Good Bye! Closing application...")
    time.sleep(2)
    sys.exit()
