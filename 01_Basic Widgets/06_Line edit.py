import sys
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QLineEdit

def line_edit_event():
    global line_edit

    print(line_edit.text()) # 창에 입력한 텍스트 터미널에 출력
    line_edit.clear() # 출력하고 삭제하기

if __name__ == '__main__':
    app = QApplication(sys.argv)

    line_edit = QLineEdit() # 입력받을 창 띄우기
    line_edit.show() # 입력받을 창 보여주기

    button = QPushButton('Button') # Button 창 띄우기
    button.show() # Button 창 보여주기
    button.clicked.connect(line_edit_event) # 버튼을 클릭하면 line_edit_event 함수 수행

    app.exec_()  # 화면 띄우고 대기하기