import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QSlider

def slider_horizon_event(): # 수평방향 함수
    global slider_horizon
    print(slider_horizon.value()) # 현재 값 터미널에 출력

def slider_vertical_event(): # 수직방향 함수
    global slider_vertical
    print(slider_vertical.value()) # 현재 값 터미널에 출력

if __name__ == '__main__':
    app = QApplication(sys.argv)

    slider_horizon = QSlider(Qt.Horizontal) # 수평방향 슬라이더 창 띄우기
    slider_horizon.setRange(0, 200) # 슬라이더 범위 정하기
    slider_horizon.show() # 수평방향 슬라이더 창 보여주기
    slider_horizon.valueChanged.connect(slider_horizon_event)

    slider_vertical = QSlider(Qt.Vertical) # 수직방향 슬라이더 창 띄우기
    slider_vertical.setRange(0, 200) # 슬라이더 범위 정하기
    slider_vertical.show() # 수직방향 슬라이더 창 보여주기
    slider_vertical.valueChanged.connect(slider_vertical_event)

    app.exec_()