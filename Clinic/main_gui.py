import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import printer_engine

class KioskApp(QWidget):
    def __init__(self):
        super().__init__()
        self.image_path = 'label.png'
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Patient ID Kiosk')
        
        # Main vertical layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(15, 15, 15, 15)

        # Input fields for patient details
        self.first_input = QLineEdit()
        self.first_input.setPlaceholderText("First Name")
        self.last_input = QLineEdit()
        self.last_input.setPlaceholderText("Last Name")
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("ID Number")

        self.main_layout.addWidget(QLabel("Enter Details:"))
        self.main_layout.addWidget(self.first_input)
        self.main_layout.addWidget(self.last_input)
        self.main_layout.addWidget(self.id_input)

        # Preview button
        self.generate_btn = QPushButton("Preview Label")
        self.generate_btn.clicked.connect(self.generate_preview)
        self.main_layout.addWidget(self.generate_btn)

        # Image preview label
        self.image_preview = QLabel("Label preview will appear here")
        self.image_preview.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.image_preview)

        # Spacer to maintain layout integrity and push buttons down nicely
        self.spacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.main_layout.addItem(self.spacer)

        # Print and Cancel buttons layout
        self.button_layout = QHBoxLayout()
        self.print_btn = QPushButton("Print (Yes)")
        self.print_btn.clicked.connect(self.action_print)
        self.cancel_btn = QPushButton("Cancel (No)")
        self.cancel_btn.clicked.connect(self.reset_ui)
        
        self.button_layout.addWidget(self.print_btn)
        self.button_layout.addWidget(self.cancel_btn)
        self.main_layout.addLayout(self.button_layout)
        
        self.setLayout(self.main_layout)
        self.print_btn.hide()
        self.cancel_btn.hide()

    def generate_preview(self):
        # Collect data from fields
        data = {
            "first": self.first_input.text(),
            "last": self.last_input.text(),
            "id": self.id_input.text()
        }
        
        # Ensure at least one field is filled
        if not any(data.values()):
            self.image_preview.setText("Error: Please fill at least one field!")
            return

        # Use the printer engine to create the label image
        printer_engine.create_label(data, self.image_path)
        
        # Load and display the created image
        pixmap = QPixmap(self.image_path)
        
        # Scale the preview smaller so it fits perfectly on the screen with the buttons
        self.image_preview.setPixmap(pixmap.scaled(300, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
        # Show buttons safely without shifting the window layout
        self.print_btn.show()
        self.cancel_btn.show()

    def action_print(self):
        # Trigger the printing process
        printer_engine.print_label(self.image_path)
        self.reset_ui()

    def reset_ui(self):
        # Clear fields and reset state
        self.first_input.clear()
        self.last_input.clear()
        self.id_input.clear()
        self.image_preview.setText("Preview will appear here")
        self.print_btn.hide()
        self.cancel_btn.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KioskApp()
    
    # FIX: Open the window in standard Maximized mode.
    # This keeps the original title bar, standard Maximize/Close buttons,
    # and leaves the top taskbar visible for your virtual keyboard.
    ex.showMaximized()
    
    sys.exit(app.exec_())
