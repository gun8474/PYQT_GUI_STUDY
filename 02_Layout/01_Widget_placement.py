import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget() # 상위 위젯
    window.resize(500, 500)

    button = QPushButton('Button', window) # window 창에 button 창 더하기
    button.move(100, 100) # 하위 위젯

    window.show()
    app.exec_()
