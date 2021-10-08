import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel

def label_event(e):
    global label

    text = label.text()
    print(text)
    label.setText(text + "!!!!")

# def event():
#     global label
#
#     str = label.text()
#     str = str + "!!!"
#     label.setText(str)
#     print(str)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    label = QLabel('Text') # Text라고 쓰인 label 창 띄우기
    label.show() # Text라고 쓰인 label 창 보여주기

    label.setStyleSheet("color: white; background-color:#0000ff")
    # 문자열 스타일 바꾸기 (글짜 색깔: 하얀색 / 배경 색깔 : 0000ff 파란색)
    label.mouseReleaseEvent = label_event

    app.exec_() # 화면 띄우고 대기하기