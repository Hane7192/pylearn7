from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def sum():
    ...

def sub():
    global a
    a = int(main_window.txt_box.text())
    main_window.txt_box.setText("")


def result():
    b = int(main_window.txt_box.text())
    c = a - b
    main_window.txt_box.setText(str(c))

app = QApplication([])

loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()

main_window.sum.clicked.connect(sum)
main_window.sub.clicked.connect(sub)
main_window.equal.clicked.connect(result)

app.exec()