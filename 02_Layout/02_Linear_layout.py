import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(500, 500)

    layout = QHBoxLayout(window) # 순차적으로 쌓아주는 방법 (수평방향)
    window.setLayout(layout) # 레이아웃이 기본 위젯에 셋팅됨

    label1 = QLabel("label1", window)
    label2 = QLabel("label2", window)
    label3 = QLabel("label3", window)

    label1.setStyleSheet("background-color:red")
    label2.setStyleSheet("background-color:orange")
    label3.setStyleSheet("background-color:yellow")

    layout.addWidget(label1)
    layout.addWidget(label2)
    layout.addWidget(label3)

    window.show()

    app.exec_()
