import sys
from PyQt5.QtWidgets import QApplication, QListWidget

def click_event():
    global list_widget
    print(list_widget.currentItem().text()) # 현재 누른 item 이름 출력
    print(list_widget.currentItem()) # 현재 누른 item 위치 출력

if __name__ == '__main__':
    app = QApplication(sys.argv)

    list_widget = QListWidget() # list 창 띄우기
    list_widget.doubleClicked.connect(click_event) # list 창 더블클릭하면 click_event 함수 수행

    items = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7", "Item8", "Item9"] # list에 들어갈 것들
    for item in items:
        list_widget.addItem(item) # list에 items 추가하기

    list_widget.show() # list 창 보여주기

    app.exec_()