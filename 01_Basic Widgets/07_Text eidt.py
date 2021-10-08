import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit

def text_edit_event():
    global text_edit

    print(text_edit.toPlainText())
    text_edit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    text_edit = QTextEdit()
    text_edit.show()

    button = QPushButton('Button') # Button 창 띄우기
    button.show() # Button 창 보여주기
    button.clicked.connect(text_edit_event) # 버튼을 클릭하면 text_edit_event 함수 수행

    app.exec_()  # 화면 띄우고 대기하기