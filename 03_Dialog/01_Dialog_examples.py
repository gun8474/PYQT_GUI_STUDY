import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(500, 500)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Message box
        self.button_message_box = QPushButton('Message box')
        self.layout.addWidget(self.button_message_box)
        self.button_message_box.clicked.connect(self.message_box_event) # 메세지박스 이벤트 버튼

        # Input dialog
        self.button_input_dialog = QPushButton('Input dialog')
        self.label_text = QLabel()
        self.layout.addWidget(self.button_input_dialog)
        self.layout.addWidget(self.label_text)
        self.button_input_dialog.clicked.connect(self.input_dialog_event)

        # File dialog
        self.button_file_dialog = QPushButton('File dialog')
        self.label_image = QLabel()
        self.pixmap = QPixmap()
        self.layout.addWidget(self.button_file_dialog)
        self.layout.addWidget(self.label_image)
        self.button_file_dialog.clicked.connect(self.file_dialog_event)

    def message_box_event(self): # 알림창 띄우기
        QMessageBox.about(self, 'About box', 'Message') # 단순 정보 전달 메세지 박스

        ret = QMessageBox.information(self, 'Information box', 'Message', QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok) # 맨 마지막 인자: 기본 설정버튼
        if ret == QMessageBox.Ok:
            print('Information box : ok')
        elif ret == QMessageBox.Cancel:
            print('Information box : cancel') # i동그라미 알림창

        ret = QMessageBox.warning(self, 'Warning box', 'Message', QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Discard)
        if ret == QMessageBox.Discard:
            print('Warning box : Discard')
        elif ret == QMessageBox.Cancel:
            print('Warning box : cancel') # !세모 알림창

        ret = QMessageBox.question(self, 'Question box', 'Message', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            print('Question box : yes')
        elif ret == QMessageBox.No:
            print('Question box : no') # ?동그라미 알림창

        ret = QMessageBox.critical(self, 'Critical box', 'Message', QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Cancel)
        if ret == QMessageBox.Discard:
            print('Warning box : Discard')
        elif ret == QMessageBox.Cancel:
            print('Warning box : cancel') # x동그라미 알림창

    def input_dialog_event(self): # 입력창 띄우기
        text, ret = QInputDialog.getText(self, 'Input dialog', 'input : ') # 입력받기 (제목, 내용)/ 어떤 버튼이 눌렸는지 반환
        if ret:
            self.label_text.setText(text) # ok버튼을 눌렀다면 입력된 메세지 띄우기

    def file_dialog_event(self): # 파일탐색기
        ret = QFileDialog.getOpenFileName(self, 'Select file') # 파일의 이름 정보 받아오기
        print(ret)

        path = ret[0]
        self.pixmap.load(path) # 경로 불러와서
        self.label_image.setPixmap(self.pixmap) # 이미지 띄우기


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
