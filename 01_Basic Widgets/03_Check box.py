import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QCheckBox

def checkbox_event():
    global checkbox

    state = checkbox.isChecked() # 체크 박스에 체크가 되어있는지 아닌지 true, false로 표현
    text = checkbox.text()
    print(state, text) # true, false 상태 + text
    checkbox.setText(text + "!!!")

def event():
    global checkbox
    state = checkbox.isChecked()
    if state: # 체크박스가 눌려있다면
        print("눌려있다")
    else: # 체크박스가 눌려있지 않다면
        print("안 눌려있다")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    checkbox = QCheckBox('Check box') # Check box 빈화면 띄우기
    checkbox.show() # 빈화면 보여주기

    checkbox.clicked.connect(checkbox_event) # 체크박스 클릭하면 함수 수행
    # checkbox.clicked.connect(event)

    app.exec_() # 화면 띄우고 대기하기