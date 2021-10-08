import sys
from PyQt5.Qt import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QTreeView
from PyQt5.QtWidgets import QPushButton

def create_model():
    model = QStandardItemModel(0, 3) # 모델 열 개수 정하기
    model.setHeaderData(0, Qt.Horizontal, "Name") # 첫번째 열
    model.setHeaderData(1, Qt.Horizontal, "Size") # 두번째 열
    model.setHeaderData(2, Qt.Horizontal, "Type") # 세번째 열
    return model # 첫번째 행 반환

def click_event(index):
    global model

    data1 = model.item(index.row(), 0).data(Qt.DisplayRole)
    data2 = model.item(index.row(), 1).data(Qt.DisplayRole)
    data3 = model.item(index.row(), 2).data(Qt.DisplayRole)
    print(data1, data2, data3)

def remove_event():
    global model, tree_view
    model.removeRow(tree_view.currentIndex().row()) # 현재 활성화된 행 삭제

if __name__ == '__main__':
    app = QApplication(sys.argv)

    tree_view = QTreeView() # 트리 창 띄우기
    model = create_model() # 첫번째 행 모델 만들기
    tree_view.setModel(model)
    tree_view.show() # 트리 창 보여주기

    tree_view.clicked.connect(click_event) # 트리 창 클릭하면 click_event 함수 수행

    model.insertRow(0)
    model.setData(model.index(0, 0), 'test.py')
    model.setData(model.index(0, 1), '100')
    model.setData(model.index(0, 2), 'python script')

    model.insertRow(0)
    model.setData(model.index(0, 0), 'image.jpg')
    model.setData(model.index(0, 1), '264')
    model.setData(model.index(0, 2), 'Image file')

    button = QPushButton('Remove') # Remove라고 쓰인 버튼 창 띄우기
    button.show() # Remove라고 쓰인 버튼 창 보여주기
    button.clicked.connect(remove_event) # 버튼 누르면 remove_event 함수 수행

    app.exec_()