import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QTreeView, QFileSystemModel
from PyQt5.QtWidgets import QLabel

def double_click_event(index):
    global model, label

    if model.isDir(index):
        print('Directory') # Directory 출력
    else:
        path = model.filePath(index)
        label.setPixmap(QPixmap(path))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    tree_view = QTreeView()
    tree_view.show()

    model = QFileSystemModel() # 파일 창 띄우기
    tree_view.setModel(model)

    root_path = "../" # 파일 경로
    model.setRootPath(root_path)
    tree_view.setRootIndex(model.index(root_path))
    tree_view.setColumnWidth(0, 400)
    tree_view.resize(700, 500)

    tree_view.setColumnHidden(1, True) # 두번째 컬럼 숨기기
    tree_view.setColumnHidden(2, True) # 세번째 컬럼 숨기기
    tree_view.setColumnHidden(3, True) # 네번째 컬럼 숨기기

    tree_view.doubleClicked.connect(double_click_event) # 트리 창 더블클릭하면 함수 double_click_event수행

    label = QLabel("label") # label 창 띄우기
    label.resize(600, 400) # label 창 크기 정하기
    label.show() # label 창 보여주기

    app.exec_()