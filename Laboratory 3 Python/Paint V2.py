from tkinter import *

root = Tk()

root.geometry("600x350")

canvas = Canvas(bg="white", width=550, height=550)
canvas.pack(anchor=CENTER, expand=1)

canvas.create_text(110, 50, text="Разработчик программы: Евгений", fill="#004D40")
canvas.create_text(2, 2, anchor=NW, text="Данная программа была создана при использовании 'Google' все права защищены.", fill="#004D40")


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.color = "black"
        self.brush_size = 2
        self.setUI()
        self.figure=self.canv.create_oval

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size 

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)
    def set_color(self, new_color):
        self.color = new_color
 
    def set_brush_size(self, new_size):
        self.brush_size = new_size
 
    def set_figure(self, new_figure):
        self.figure = new_figure



    def setUI(self):

        self.parent.title("Paint")  # Устанавливаем название окна
        self.pack(fill=BOTH, expand=1)  # Размещаем активные элементы на родительском окне

        self.columnconfigure(6, weight=1) # Даем седьмому столбцу возможность растягиваться, благодаря чему кнопки не будут разъезжаться при ресайзе
        self.rowconfigure(2, weight=1) # То же самое для третьего ряда

        self.canv = Canvas(self, bg="white")  # Создаем поле для рисования, устанавливаем белый фон
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E+W+S+N)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна
        self.canv.bind("<B1-Motion>", self.draw) # Привязываем обработчик к канвасу. <B1-Motion> означает "при движении зажатой левой кнопки мыши" вызывать функцию draw

        color_lab = Label(self, text="Color: ") # Создаем метку для кнопок изменения цвета кисти
        color_lab.grid(row=0, column=0, padx=6) # Устанавливаем созданную метку в первый ряд и первую колонку, задаем горизонтальный отступ в 6 пикселей

        red_btn = Button(self, text="Red", width=6,
                         command=lambda: self.set_color("Red")) # Создание кнопки:  Установка текста кнопки, задание ширины кнопки (10 символов), функция вызываемая при нажатии кнопки.
        red_btn.grid(row=0, column=1) # Устанавливаем кнопку
        

        # Создание остальных кнопок повторяет ту же логику, что и создание
        # кнопки установки красного цвета, отличаются лишь аргументы.

        green_btn = Button(self, text="Green", width=5,
                           command=lambda: self.set_color("Green"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, text="Blue", width=5,
                          command=lambda: self.set_color("Blue"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, text="Black", width=5,
                           command=lambda: self.set_color("Black"))
        black_btn.grid(row=0, column=4)

        purple_btn = Button(self, text="Purple", width=5,
                           command=lambda: self.set_color("Purple"))
        purple_btn.grid(row=0, column=5)

        white_btn = Button(self, text="White", width=5,
                           command=lambda: self.set_color("White"))
        white_btn.grid(row=0, column=8)

        

        clear_btn = Button(self, text="Удалить всё", width=10,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=7, sticky=W)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="2", width=5,
                         command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="5", width=5,
                         command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)

        five_btn = Button(self, text="7", width=5,
                          command=lambda: self.set_brush_size(7))
        five_btn.grid(row=1, column=3)

        seven_btn = Button(self, text="10", width=5,
                           command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=1, column=4)

        ten_btn = Button(self, text="20", width=5,
                         command=lambda: self.set_brush_size(20))
        ten_btn.grid(row=1, column=5)

        twenty_btn = Button(self, text="50", width=5,
                            command=lambda: self.set_brush_size(50))
        twenty_btn.grid(row=1, column=6, sticky=W)


        figure = Button(self, text='pan', width=10, command=lambda: self.set_figure("pan") )
        figure.grid(row=3, column=1, sticky=W)
 
        figure = Button(self,text = 'line', width=10, command = lambda: self.set_figure("line"))
        figure.grid(row = 3, column = 2,sticky=W)
 
        figure = Button(self,text = 'oval', width=10, command = lambda: self.set_figure("oval") )
        figure.grid(row = 3, column = 3,sticky=W)
 
        figure = Button(self,text = 'rectangle', width=10, command = lambda: self.set_figure("rectangle"))
        figure.grid(row = 3, column = 4,sticky=W)
            

  
def main():
    root=Tk()
    root.geometry("1280x300+500+400")
    app=Paint(root)
    root.mainloop()

if __name__ == '__main__':
    main()
