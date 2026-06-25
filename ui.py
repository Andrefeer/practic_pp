import tkinter as tk
import pygubu
import random

import tkinter as tk
import pygubu
import random


class App:
    def __init__(self, master):
        self.builder = pygubu.Builder()
        self.builder.add_from_file("test_ui.ui")

        self.mainwindow = self.builder.get_object("Stack_app_window", master)

        self.a_var = self.builder.get_variable("a")
        self.b_var = self.builder.get_variable("b")

        self.result = self.builder.get_object("result")

        self.builder.connect_callbacks(self)

        self.a_list = []
        self.b_list = []

    def gen_a(self):
        self.a_list = random.sample(range(1, 50), 5)
        self.a_var.set(str(self.a_list))

    def gen_b(self):
        self.b_list = random.sample(range(1, 50), 5)
        self.b_var.set(str(self.b_list))

    def union(self):
        res = list(set(self.a_list) | set(self.b_list))

        self.result.delete("1.0", "end")
        self.result.insert("end", str(res))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()