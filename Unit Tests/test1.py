"""
Hardware Unit Test: Touchscreen Input Digitizer
This script scans the Linux input device tree to verify that the touch panel hardware 
is properly recognized as an input layer (specifically detecting the ft5x06 touch chip).
"""

import subprocess

def check_touch_digitizer():
    print("--- HARDWARE TEST: TOUCH DIGITIZER ---")
    
    try:
        # Querying the Linux proc file system for connected input hardware devices
        devices = subprocess.run(
            ['cat', '/proc/bus/input/devices'], 
            capture_output=True, 
            text=True, 
            timeout=5
        )
        
        output_lower = devices.stdout.lower()
        
        # Checking for capacitive touch signatures including the specific ft5x06 controller
        if any(keyword in output_lower for keyword in ["touch", "digitizer", "touchscreen", "ft5x06"]):
            print("SUCCESS: Touch hardware digitizer discovered in system input devices.")
            return True
        else:
            print("FAIL: Screen may display an image, but the touch component is not registered by Linux.")
            return False
            
    except Exception as e:
        print(f"ERROR: Failed to query system input devices: {e}")
        return False

if __name__ == "__main__":
    check_touch_digitizer()