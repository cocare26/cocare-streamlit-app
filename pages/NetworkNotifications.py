from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class NetworkNotificationsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Network Notifications")
        self.setGeometry(300, 100, 500, 500)
        self.setStyleSheet("background-color: #eaf6ff;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        title = QLabel("Network Notifications")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #2196f3;")

        notif1 = QLabel("• No network problems detected")
        notif2 = QLabel("• Latest update installed")
        notif3 = QLabel("• Signal strength is excellent")

        labels = [notif1, notif2, notif3]

        for lbl in labels:
            lbl.setFixedHeight(50)
            lbl.setStyleSheet('''
                background-color: white;
                border-radius: 12px;
                padding-left: 15px;
                font-size: 15px;
                color: #2196f3;
                border: 1px solid #64b5f6;
            ''')
            layout.addWidget(lbl)

        layout.addWidget(title)
        layout.addSpacing(20)

        central_widget.setLayout(layout)
