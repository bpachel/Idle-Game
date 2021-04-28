import tkinter as tk
from tkinter import font as tkfont


class Application(tk.Tk):
    # Tutaj przekazujemy logikę
    # def __init__(self, game, *args, **kwargs):
    def __init__(self, *args, **kwargs):
        """Konstruktor dla Application.
        Tworzy wszystkie strony oraz kontener, w którym będą one umieszczone. Ustawia 
        i konfiguruje domyślne wartości, umieszcza kontener oraz strony na ekranie.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.main_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.create_frames()
        self.show_frame("MainWindow")

    def create_frames(self):
        """zainicjalizuj wszystkie strony i umieść je jedna na drugiej"""
        for F in (MainWindow, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            # umieść wszystkie strony w tym samym miejscu
            # widoczna będzie ta strona, która jest na wierzchu
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        """Umieść daną stronę na wierzchu stosu, tak aby była widoczna
        Args:
            page_name: str, nazwa strony
        """
        frame = self.frames[page_name]
        frame.tkraise()

    def reset_all(self):
        """zresetuj wszystkie strony"""
        pass

    def update_frame(self, page_name):
        """Uaktualnij daną stronę
        Args:
            page_name: str, nazwa strony
        """
        frame = self.frames[page_name]
        frame.update()


class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        """Konstruktor dla MainWindow.
        Args:
            parent: tk.Frame, kontener będący rodzicem strony.
            controller: Application, instancja klasy bazowej
        """

        tk.Frame.__init__(self, parent)
        self.controller = controller

        bg_image = tk.PhotoImage(\
            file=r"C:\Users\matht\Downloads\Materiały_Monaker_UI_1\validation.png")
        x = tk.Label(self, image=bg_image)
        x.place(x=0, y=0, relwidth=1, relheight=1)
        x.image = bg_image

        some_lb = tk.Label(self, text='Menu', font=controller.main_font)
        newGame_btn = tk.Button(self, text="New Game", font=controller.main_font,
                                command=lambda: controller.show_frame("PageOne"))
        exitGame_btn = tk.Button(self, text="Exit", font=controller.main_font,
                                command=lambda: controller.show_frame("PageOne"))

        some_lb.grid(row=2, column=2, sticky='nesw')
        newGame_btn.grid(row=4, column=2, sticky='ew')
        exitGame_btn.grid(row=6, column=2, sticky='ew')

        for x in range(10):
            self.rowconfigure(x, weight=1)
        for y in range(5):
            self.columnconfigure(y, weight=1)

    def update(self):
        """Uaktualnij dane na stronie"""
        pass

    def reset(self):
        """Zresetuj stronę do stanu początkowego"""
        pass


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        """Konstruktor dla PageOne.
        Args:
            parent: tk.Frame, kontener będący rodzicem strony.
            controller: Application, instancja klasy bazowej
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.entry_label_font = tkfont.Font(
            family='Helvetica', size=12, weight='bold')

        some_lb = tk.Label(self, text='Game', font=controller.main_font)
        pageTwo_btn = tk.Button(self, text="finish game", font=controller.main_font,
                                command=lambda: controller.show_frame("PageTwo"))

        some_lb.grid(row=0, column=0)
        pageTwo_btn.grid(row=1, column=0)

    def update(self):
        """Uaktualnij dane na stronie"""
        pass

    def reset(self):
        """Zresetuj stronę do stanu początkowego"""
        pass


class PageTwo(tk.Frame):
    """Okno ekranu końcowego.
    Attributes:
        controller: Application, odpowiada argumentowi dostarczonemu w konstruktorze,
            instancja klasy bazowej
    """

    def __init__(self, parent, controller):
        """Konstruktor dla PageTwo.
        Tworzy przyciski i etykiety, rozmieszcza elementy na stronie.
        Args:
            parent: tk.Frame, kontener będący rodzicem strony.
            controller: Application, instancja klasy bazowej
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        some_lb = tk.Label(self, text='Game Over', font=controller.main_font)
        mainWindow_btn = tk.Button(self, text="Restart", font=controller.main_font,
                                   command=lambda: controller.show_frame("MainWindow"))

        some_lb.grid(row=0, column=0)
        mainWindow_btn.grid(row=1, column=0)

    def update(self):
        """Uaktualnij dane na stronie"""
        pass

    def reset(self):
        """Zresetuj stronę do stanu początkowego"""
        pass


def main():
    # app = Application(game)
    app = Application()
    app.geometry("500x400")
  
    app.mainloop()


if __name__ == "__main__":

    main()
