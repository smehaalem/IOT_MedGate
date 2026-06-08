"""
Hardware Unit Test: Printer USB Connectivity
This script scans the local hardware USB bus topology using system CLI calls 
to ensure that the Brother QL printer is physically attached and electrically powered.
"""

import subprocess

def check_printer_usb():
    print("--- HARDWARE TEST: PRINTER USB CONNECTIVITY ---")
    
    try:
        # Executing the list USB utility to find connected peripheral devices
        usb_scan = subprocess.run(['lsusb'], capture_output=True, text=True, timeout=5)
        
        # Validating the presence of the Brother manufacturing vendor signature
        if "brother" in usb_scan.stdout.lower():
            print("SUCCESS: Brother Printer hardware communication via USB is verified.")
            
            # Extract and print the specific log line containing the printer info
            matching_lines = [line for line in usb_scan.stdout.splitlines() if "brother" in line.lower()]
            if matching_lines:
                print(f"Device Details: {matching_lines[0]}")
            return True
        else:
            print("FAIL: Brother Printer not detected on the USB bus. Verify cable connection and power switch.")
            return False
            
    except Exception as e:
        print(f"ERROR: Failed to run hardware USB scan: {e}")
        return False

if __name__ == "__main__":
    check_printer_usb()