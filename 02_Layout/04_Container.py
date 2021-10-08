import sys
from PyQt5.QtWidgets import QApplication, QGroupBox, QVBoxLayout, QScrollArea, QWidget, \
    QHBoxLayout, QTabWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget() # 디자인적인 요소를 집어넣음
    window.resize(400, 400)
    window.show()

    main_layout = QHBoxLayout()
    window.setLayout(main_layout)

    # Group box
    group_box = QGroupBox('Group name') # 위젯들의 그룹을 생성하고 이름을 설정
    group_layout = QVBoxLayout(group_box) # 박스 레이아웃이 그룹 레이아웃에 포함 (수직방향으로 정렬)
    group_layout.addWidget(QPushButton('Group box button')) # 버튼 생성하여 그룹박스안에 집어넣음
    main_layout.addWidget(group_box)

    # Scroll area
    scroll_area = QScrollArea() # 위젯들을 포함하는 영역 생성 (영역이 작은 경우 자동으로 스크롤 생성)
    label = QLabel("a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz")
    scroll_area.setWidget(label) # 라벨 위젯을 셋팅하고
    main_layout.addWidget(scroll_area) # 스크롤 위젯에 추가
    # main_layout.addWidget(label)

    # Tab
    tab_widget = QTabWidget() # 여러개의 탭(중첩 위젯) 생성
    tab1 = QPushButton('Tab1 button') # 탭1 버튼 생성
    tab_widget.addTab(tab1, 'Tab 1') # 탭 위젯 추가

    tab2 = QWidget() # 위젯 생성
    tab_layout = QVBoxLayout(tab2)
    tab_layout.addWidget(QLabel('Tab2 label'))
    tab_layout.addWidget(QPushButton('Tab2 button'))
    tab_widget.addTab(tab2, 'Tab 2')

    main_layout.addWidget(tab_widget)

    app.exec_()
