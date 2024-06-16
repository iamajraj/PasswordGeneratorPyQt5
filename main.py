import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QSpinBox, QCheckBox
from PyQt5.QtCore import Qt

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Generator')
        self.setGeometry(100, 100, 400, 300)
        
        self.github_username = 'iamajraj'
        
        self.setupUI()
        
    def setupUI(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        main_widget.setLayout(layout)
        
        # Title label
        title_label = QLabel('Password Generator')
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # GitHub link label
        github_label = QLabel(f'GitHub: <a href="https://github.com/{self.github_username}">{self.github_username}</a>')
        github_label.setOpenExternalLinks(True)
        github_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(github_label)
        
        # Length input
        length_label = QLabel('Password Length:')
        layout.addWidget(length_label)
        
        self.length_spinbox = QSpinBox()
        self.length_spinbox.setMinimum(6)
        self.length_spinbox.setMaximum(30)
        self.length_spinbox.setValue(12)
        layout.addWidget(self.length_spinbox)
        
        # Character type checkboxes
        self.uppercase_checkbox = QCheckBox('Include Uppercase')
        self.lowercase_checkbox = QCheckBox('Include Lowercase')
        self.digits_checkbox = QCheckBox('Include Digits')
        self.symbols_checkbox = QCheckBox('Include Symbols')
        
        self.uppercase_checkbox.setChecked(True)
        self.lowercase_checkbox.setChecked(True)
        self.digits_checkbox.setChecked(True)
        self.symbols_checkbox.setChecked(False)
        
        checkboxes_layout = QHBoxLayout()
        checkboxes_layout.addWidget(self.uppercase_checkbox)
        checkboxes_layout.addWidget(self.lowercase_checkbox)
        checkboxes_layout.addWidget(self.digits_checkbox)
        checkboxes_layout.addWidget(self.symbols_checkbox)
        layout.addLayout(checkboxes_layout)
        
        # Generate button
        generate_button = QPushButton('Generate Password')
        generate_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px;")
        generate_button.clicked.connect(self.generate_password)
        layout.addWidget(generate_button)
        
        # Copy button
        copy_button = QPushButton('Copy Password')
        copy_button.setStyleSheet("background-color: #008CBA; color: white; padding: 10px 20px; border: none; border-radius: 5px;")
        layout.addWidget(copy_button)
        
        # Result display label
        self.result_label = QLabel('Generated Password will appear here.')
        self.result_label.setStyleSheet("font-size: 14px; margin-top: 20px; padding: 10px; border: 1px solid #ccc; border-radius: 5px;")
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)
        
    def generate_password(self):
        length = self.length_spinbox.value()
        include_uppercase = self.uppercase_checkbox.isChecked()
        include_lowercase = self.lowercase_checkbox.isChecked()
        include_digits = self.digits_checkbox.isChecked()
        include_symbols = self.symbols_checkbox.isChecked()
        
        characters = ''
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
        
        if characters:
            generated_password = ''.join(random.choice(characters) for _ in range(length))
            self.result_label.setText(f"Generated Password: {generated_password}")
            self.copied_password = generated_password
        else:
            self.result_label.setText("Please select at least one character type.")
            self.copied_password = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("QMainWindow { background-color: #f0f0f0; }")
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
