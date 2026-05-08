from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class RenewalsTariffWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Renewals & Tariff Changes")
        self.setGeometry(300, 100, 500, 500)
        self.setStyleSheet("background-color: #eaf6ff;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout() 
       

# زر الرجوع
back_btn = QPushButton("⬅ Back")

back_btn.setFixedHeight(40)

back_btn.setStyleSheet('''
    QPushButton {
        background-color: white;
        border-radius: 12px;
        font-size: 14px;
        color: #2196f3;
        border: 2px solid #64b5f6;
        padding-left: 10px;
        text-align: left;
    }

    QPushButton:hover {
        background-color: #bbdefb;
    }
''')

back_btn.clicked.connect(self.close)

layout.addWidget(back_btn)

        title = QLabel("Renewals & Tariff Changes")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #2196f3;")

        renew_btn = QPushButton("Renew Current Package")
        tariff_btn = QPushButton("Change Tariff")
        history_btn = QPushButton("View Renewal History")

        buttons = [renew_btn, tariff_btn, history_btn]

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
