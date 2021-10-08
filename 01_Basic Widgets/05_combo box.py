import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QComboBox

def combobox_event():
    global combobox

    index = combobox.currentIndex() # combobox 클릭한 번째
    text = combobox.currentText() # 클릭한 combobox 이름
    print(index, " : ", text)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    combobox_items = ["Item1", "Item2", "Item3"] # combobox에 들어갈 것들
    combobox = QComboBox() # QComboBox 화면 띄우기
    for item in combobox_items:
        combobox.addItem(item)
    combobox.show() # QComboBox 회면 보여주기

    combobox.currentIndexChanged.connect(combobox_event)

    app.exec_()  # 화면 띄우고 대기하기