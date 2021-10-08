import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton

def button_event():
    print('button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    button = QPushButton('Button') # Button이라고 쓰인 빈화면 띄우기
    button.show() # 빈화면 보여주기

    button.clicked.connect(button_event) # 버튼 누르면 터미널에 button click 출력

    app.exec_() # 화면 띄우고 대기하기