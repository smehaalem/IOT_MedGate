# MedGate - Clinic Core Application

This directory contains the main source code and executable scripts for the MedGate kiosk and clinic management system. 

## 📁 Directory Structure

* `main_gui.py`: The main entry point of the application. It runs the PyQt5 graphical user interface (touchscreen optimized).
* `label_manager.py`: Handles data processing, QR code generation, and communicates with the CUPS service to print physical labels.
  

## 🛠️ Prerequisites & Dependencies

To run the application locally on the Raspberry Pi, ensure you have Python 3 installed along with the following libraries and tools:

* **PyQt5** - For the graphical user interface.
* **qrcode** - For generating patient and inventory QR codes.
* **Pillow (PIL)** - For creating and formatting the label images.

*(Note: CUPS and the Brother printer drivers must be configured on the OS level for the print module to work).*

## 🚀 How to Run

Navigate to this directory in your terminal and run the main GUI script:

```bash
python3 main_gui.py
