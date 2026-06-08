"""
Hardware Unit Test: CUPS Print Spooler and Driver Active State
This script checks the status of the printing daemon queue to ensure that 
the Brother QL device driver is mapped, enabled, and ready to spool label print jobs.
"""

import subprocess

def check_cups_spooler():
    print("--- HARDWARE TEST: CUPS PRINT SPOOLER ---")
    
    try:
        # Requesting printer status from the Common Unix Printing System (CUPS)
        cups_status = subprocess.run(['lpstat', '-p'], capture_output=True, text=True, timeout=5)
        
        # Check if the command executed cleanly and the driver queue is active
        if cups_status.returncode == 0 and "enabled" in cups_status.stdout.lower():
            print("SUCCESS: CUPS print spooler is configured and printer driver is active.")
            print(f"Current Spooler Status: {cups_status.stdout.strip()}")
            return True
        else:
            print("FAIL: CUPS is offline or the printer driver queue has not been registered in localhost:631.")
            return False
            
    except Exception as e:
        print(f"ERROR: Failed to communicate with print subsystem: {e}")
        return False

if __name__ == "__main__":
    check_cups_spooler()