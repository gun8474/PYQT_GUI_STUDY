import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel

def pixmap_event():
    global button

    pixmap = QPixmap('../01_Basic Widgets/image.jpg') # 이미지가 있는 파일 경로 설정
    label.setPixmap(pixmap) # Button을 클리하면 label 창에 이미지를 불러옴

if __name__ == '__main__':
    app = QApplication(sys.argv)

    label = QLabel('Label') # label 창 띄우기
    button = QPushButton('Button') # button 창 띄우기
    button.clicked.connect(pixmap_event) # button 창을 누르면 pixmap_event 함수 수행
    label.show() # label 창 보여주기
    button.show() # button 창 보여주기

    app.exec_()  # 화면 띄우고 대기하기