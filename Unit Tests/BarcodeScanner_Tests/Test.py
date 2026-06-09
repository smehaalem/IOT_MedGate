"""
Hardware Unit Test: GM65 Barcode Scanner (Functional Read Test)
This script verifies the actual reading capability of the scanner.
Since the scanner emulates a USB keyboard, it waits for standard input,
captures the scanned string, and validates the output.
"""

import sys

def run_functional_test():
    print("--- GM65 Scanner Functional Read Test ---")
    print("Please scan any barcode now (e.g., from a product, phone screen, or ID)...")
    
    try:
        # The script waits here. When you scan, the GM65 types the barcode and sends 'Enter'
        barcode_data = input("Waiting for scan >> ")

        if barcode_data.strip():
            print("\n[SUCCESS] Barcode successfully read and received!")
            print(f"-> Scanned Data: '{barcode_data}'")
            print(f"-> Length: {len(barcode_data)} characters")
            sys.exit(0)
        else:
            print("\n[FAIL] Empty data received. The scanner fired an event but sent no text.")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n[INFO] Test cancelled by the user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred during scanning: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_functional_test()
