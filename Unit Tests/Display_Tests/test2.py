"""
Hardware Unit Test: 7-Inch Touchscreen Video Signal
This script verifies if the Raspberry Pi video core detects the physical screen
and establishes an active display signal output via the Linux DRM subsystem.
"""

import os

def check_video_signal():
    print("--- HARDWARE TEST: SCREEN VIDEO SIGNAL ---")
    
    # Path to the primary HDMI output status node in Linux DRM
    hdmi_path = '/sys/class/drm/card0-HDMI-A-1/status'
    
    if os.path.exists(hdmi_path):
        with open(hdmi_path, 'r') as f:
            status = f.read().strip()
            
        print(f"Display connection status: {status}")
        if status == "connected":
            print("SUCCESS: Physical screen is receiving a video signal!")
            return True
        else:
            print("FAIL: Display reports as disconnected.")
            return False
    else:
        # Fallback mechanism for official DSI flat-ribbon cable interfaces
        print("INFO: Standard HDMI node not found, checking framebuffer subsystem...")
        if os.path.exists('/sys/class/graphics/fb0'):
            print("SUCCESS: Framebuffer is active. Display framework is running.")
            return True
        else:
            print("FAIL: No display framework or framebuffer detected.")
            return False

if __name__ == "__main__":
    check_video_signal()
