import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QFileDialog, QPushButton
from PyQt5.QtWidgets import QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        # Actions
        self.action_load = QAction(QIcon('../images/icons/save.png'), 'Load file', self) # 아이콘 설정 가능, 기능 설명
        self.action_load.setShortcut('Ctrl+L') # Load 단축키 지정 (안해도 상관 없음)
        self.action_load.triggered.connect(self.load_event)

        self.action_exit = QAction(QIcon('../images/icons/exit.png'), 'Exit', self)
        self.action_exit.setShortcut('ESC') # 종료 단축기 지정
        self.action_exit.triggered.connect(self.close) # close 기본 함수 연결

        # Status bar 선택한 항목의 상태 보여주기
        self.status_bar = self.statusBar()

        # Menu bar
        self.menu_bar = self.menuBar() # menuBar를 이용해 객체 불러오기
        self.file_menu = self.menu_bar.addMenu('File')
        self.option_menu = self.menu_bar.addMenu('Options')

        self.file_menu.addAction(self.action_load)
        self.file_menu.addAction(self.action_exit)

        # Tool bar 기능을 가진 아이콘들을 모은 바
        self.tool_bar = self.addToolBar("Toolbar")
        self.tool_bar.addAction(self.action_load) # 툴바에 액션 추가
        self.tool_bar.addAction(self.action_exit) # 툴바에 액션 추가

        # Central Widget
        window_widget = QWidget()
        window_layout = QVBoxLayout(window_widget)
        window_layout.addWidget(QPushButton("Button"))
        self.setCentralWidget(window_widget) # 위젯을 전달해주면 만들어놓은 위젯을 포함시켜줌

    def load_event(self):
        self.status_bar.showMessage("Load file..") # 메세지 보여주기
        path = QFileDialog.getOpenFileName(self) # 파일 불러와서
        print(path) # 경로 띄우기
        self.status_bar.clearMessage() # 메세지 지우기


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
