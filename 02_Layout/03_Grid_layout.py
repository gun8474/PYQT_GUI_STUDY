import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QSizePolicy

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(500, 500)

    layout = QGridLayout(window) # 네모칸으로 만들어놓고 그 안에 위젯을 하나씩 추가하는 방법
    window.setLayout(layout)

    label1 = QLabel("label1", window)
    label2 = QLabel("label2", window)
    label3 = QLabel("label3", window)

    label1.setStyleSheet("background-color:red")
    label2.setStyleSheet("background-color:orange")
    label3.setStyleSheet("background-color:yellow")

    layout.addWidget(label1, 0, 0) # 박스는 순차적으로 쌓이지만 그리드는 위젯의 행렬의 정보를 주어 위치를 지정할 수 있음 (0행 0열)
    layout.addWidget(label2, 0, 1) # 0행 1열
    # layout.addWidget(label3, 1, 1) # 1행 1열
    layout.addWidget(label3, 1, 0, 1, 2) # 행, 열, 행방향 몇칸, 열방향 몇칸

    window.show()

    app.exec_()
