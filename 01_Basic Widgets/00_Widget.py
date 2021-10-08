import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QWidget() # 빈화면 띄우기
    widget.show() # 빈화면 보여주기

    # widget.setWindowTitle("GUI program") # 윈도우 타이틀 지정하기
    # widget.move(200, 200) # 윈도우 위치 조정하기
    # widget.resize(200, 200) # 윈도우 사이즈 조정하기

    # widget.setGeometry(200, 200, 400, 200) # 한 줄로 줄여서 쓰기 (위치, 크기)

    app.exec_() # 화면 띄우고 대기하기


