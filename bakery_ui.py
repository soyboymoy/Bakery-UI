import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')
        Label(window, text='샌드위치 (5000원)').grid(column=0, row=0)
        Label(window, text='케이크 (20000원)').grid(column=0, row=1)
        num_s = Entry(window, width=10)
        num_c = Entry(window, width=10)
        num_s.grid(column=1, row=0)
        num_c.grid(column=1, row=1)
        btn_order = Button(window, text="주문하기", command=lambda: CustomerView.send_order(self, num_s.get(), num_c.get()))
        btn_order.grid(column=0, row=2)

    def send_order(self, ns, nc):
        order_text = ""
        if ns.isdigit():
            if int(ns) != 0:
                order_text += "샌드위치 (5000원) " + ns + "개"
        if nc.isdigit():
            if int(nc) != 0:
                if "샌드위치" in order_text:
                    order_text += ", 케이크 (20000원) " + nc + "개"
                else:
                    order_text += "케이크 (20000원) " + nc + "개"
        if order_text != "":
            order_text = str(self.name) + " " + order_text
            self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
