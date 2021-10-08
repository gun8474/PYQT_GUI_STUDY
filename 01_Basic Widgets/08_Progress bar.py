import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QProgressBar

def progress_event():
    global progress

    val = progress.value() # 현재 진행률
    progress.setValue(val+10) # 현재 진행률에 10씩 더하기

if __name__ == '__main__':
    app = QApplication(sys.argv)

    progress = QProgressBar() # 진행창 띄우기

    progress.setRange(1, 100) # 진행창의 범위 정하기
    progress.reset()
    # or
    # progress.setRange(0, 0) # 계속해서 바 채우기

    progress.show() # 진행창 보여주기

    button = QPushButton('Button') # Button 창 띄우기
    button.show() # Button 창 보여주기
    button.clicked.connect(progress_event) # 버튼을 클릭하면 progress_event 함수 수행

    app.exec_()  # 화면 띄우고 대기하기