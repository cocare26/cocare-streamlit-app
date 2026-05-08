from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class InternetPackagesWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Internet Packages")
        self.setGeometry(300, 100, 500, 500)
        self.setStyleSheet("background-color: #eaf6ff;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        title = QLabel("Internet Packages")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #2196f3;")

        package1 = QPushButton("6 GB Package - 5 JD")
        package2 = QPushButton("15 GB Package - 10 JD")
        package3 = QPushButton("Unlimited Package - 25 JD")

        buttons = [package1, package2, package3]

        for btn in buttons:
            btn.setFixedHeight(60)
            btn.setStyleSheet('''
                QPushButton {
                    background-color: white;
                    border-radius: 15px;
                    font-size: 16px;
                    color: #2196f3;
                    border: 2px solid #64b5f6;
                }
                QPushButton:hover {
                    background-color: #bbdefb;
                }
            ''')
            layout.addWidget(btn)

        layout.addWidget(title)
        layout.addSpacing(20)

        central_widget.setLayout(layout)
