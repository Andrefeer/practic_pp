import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QTextEdit, QGridLayout
)


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stack App PyQt5")

        # date
        self.a_list = []
        self.b_list = []

        # UI elements
        self.label_title_a = QLabel("Multimea A:")
        self.label_title_b = QLabel("Multimea B:")

        self.label_a = QLabel("-")
        self.label_b = QLabel("-")

        self.btn_gen_a = QPushButton("Genereaza A")
        self.btn_gen_b = QPushButton("Genereaza B")
        self.btn_union = QPushButton("Calculeaza")

        self.result = QTextEdit()
        self.result.setReadOnly(True)

        # layout (echivalent grid din pygubu)
        layout = QGridLayout()

        layout.addWidget(self.label_title_a, 0, 0)
        layout.addWidget(self.label_a, 0, 1)
        layout.addWidget(self.btn_gen_a, 0, 3)

        layout.addWidget(self.label_title_b, 1, 0)
        layout.addWidget(self.label_b, 1, 1)
        layout.addWidget(self.btn_gen_b, 1, 3)

        layout.addWidget(self.result, 2, 0, 1, 3)
        layout.addWidget(self.btn_union, 2, 3)

        self.setLayout(layout)

        # events (callback echivalent)
        self.btn_gen_a.clicked.connect(self.gen_a)
        self.btn_gen_b.clicked.connect(self.gen_b)
        self.btn_union.clicked.connect(self.union)

    def gen_a(self):
        self.a_list = random.sample(range(1, 50), 5)
        self.label_a.setText(str(self.a_list))

    def gen_b(self):
        self.b_list = random.sample(range(1, 50), 5)
        self.label_b.setText(str(self.b_list))

    def union(self):
        res = list(set(self.a_list) | set(self.b_list))
        self.result.setText(str(res))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())