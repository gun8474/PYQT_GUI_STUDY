import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout

class MainWindow(QWidget): # 함수 상속
    def __init__(self):
        super().__init__()

        # 이쪽에 원하는 구문을 쓰면 메인함수에서는 깔끔하게 코딩가능
        main_layout = QVBoxLayout(self)
        layout = QHBoxLayout()

        label1 = QLabel("label1")
        label2 = QLabel("label2")
        label3 = QLabel("label3")
        label1.setStyleSheet("background-color:red")
        label2.setStyleSheet("background-color:orange")
        label3.setStyleSheet("background-color:yellow")

        main_layout.addWidget(label1)
        # main_layout.addWidget(label2)
        # main_layout.addWidget(label3)
        layout.addWidget(label2)
        layout.addWidget(label3)
        main_layout.addLayout(layout)

# Layout 중첩, QWidget 상속
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # window = QWidget()
    # or
    window = MainWindow()
    window.show()

    app.exec_()
