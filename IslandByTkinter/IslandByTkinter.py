import tkinter as tk
from tkinter import ttk
from tkinter import Canvas, Text

import Main


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Island')
        self.geometry('500x500+500+200')

        self.convas = Canvas(self, width=500, height=400, bg="#5cbcfc")

        self.label1 = ttk.Label(self)
        self.label2 = ttk.Label(self)
        self.label3 = ttk.Label(self)

        self.text = Text(self, height=20, width=50)
        self.text.pack(expand=True)

        self.button = ttk.Button(self, text="Show", command=self.get_input)
        self.button.pack(expand=True)

    def get_input(self):

        matrix = []
        value = self.text.get(1.0, "end-1c").split()
        row_number, column_number = map(int, value[:2])
        s = 2
        e = 2 + column_number
        for i in range(row_number):
            matrix.append(list(map(int, value[s:e])))
            s = e
            e += column_number

        self.show_land(matrix)
        self.show_anwser(matrix)

    def show_land(self, matrix):
        """ hide textbox and button """
        self.text.pack_forget()
        self.button.pack_forget()
        self.convas.pack()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    x0 = (j * 10) + 150
                    y0 = (i * 10) + 100
                    x1 = (j * 10) + 145
                    y1 = (i * 10) + 95
                    self.convas.create_oval(x0, y0, x1, y1, fill="#000")

    def show_anwser(self, matrix):

        resault = Main.solve(matrix)

        x0 = (resault[0][1] * 10) + 150
        y0 = (resault[0][0] * 10) + 100
        x1 = (resault[1][1] * 10) + 145
        y1 = (resault[1][0] * 10) + 95
        self.convas.create_line(x0, y0, x1, y1)

        self.label1.config(text=f"az deraye : {resault[0]}")
        self.label2.config(text=f"ta deraye : {resault[1]}")
        self.label3.config(text=f"fasele : {resault[2]}")

        self.label1.pack(expand=True)
        self.label2.pack(expand=True)
        self.label3.pack(expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
