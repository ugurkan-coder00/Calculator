from tkinter import *
import os,random

class Calculator:
    def __init__(self) -> None:
        self.title = "Calculator"
        self.geometry = {
            "x":"350",
            "y":"290"
        }
        self.color = "gray2"
        self.Window()
        self.Screen()
        self.Buttons()
        self.Window_Loop()

    def Window(self):
        self.root = Tk()
        self.root.title(self.title)
        self.root.geometry(f"{self.geometry['x']}x{self.geometry['y']}")
        self.root.configure(bg = self.color)
        self.root.resizable(0,0)

    def Screen(self):
        self.screen = Entry(
            self.root,
            bg = "gray98",
            fg = "purple",
            highlightthickness=0,
            borderwidth=0,
            justify=RIGHT,
            font = ("Arial",20,"bold"),
            insertbackground="gray98"
        )
        self.screen.pack()
        self.screen.place(x = 10,y = 10,width=330,height=35)
    
    def Buttons(self):
        def command(event):
            self.screen.insert(END,event)

        def delete_object():
            self.screen.delete(0,END)

        def main_command():
            try:
                data = self.screen.get()
                islem = eval(data)
                self.screen.delete(0,END)
                self.screen.insert(0,islem)
            except NameError:
                self.screen.delete(0,END)
                self.screen.insert(0,"VALUE_ERROR")
            except SyntaxError:
                self.screen.delete(0,END)
                self.screen.insert(0,"VALUE_ERROR")
        #region Buttons
        self.button_one = Button(self.root,highlightthickness=0,borderwidth=0,bg = "gray10",fg = "white",text = "1",font = ("Arial",15,"bold"),command=lambda:command("1"))
        self.button_one.pack()
        self.button_one.place(x = 10,y =60,height=40,width=50)

        self.button_two = Button(self.root,highlightthickness=0,borderwidth=0,bg = "gray10",fg = "white",text = "2",font = ("Arial",15,"bold"),command=lambda:command("2"))
        self.button_two.pack()
        self.button_two.place(x = 80,y =60,height=40,width=50)

        self.button_thr = Button(self.root,highlightthickness=0,borderwidth=0,bg = "gray10",fg = "white",text = "3",font = ("Arial",15,"bold"),command=lambda:command("3"))
        self.button_thr.pack()
        self.button_thr.place(x = 150,y =60,height=40,width=50)

        self.button_for = Button(self.root,highlightthickness=0,borderwidth=0,bg = "gray10",fg = "white",text = "4",font = ("Arial",15,"bold"),command=lambda:command("4"))
        self.button_for.pack()
        self.button_for.place(x = 10,y =120,height=40,width=50)
        
        self.button_five = Button(self.root,highlightthickness=0,borderwidth=0,bg = "gray10",fg = "white",text = "5",font = ("Arial",15,"bold"),command=lambda:command("5"))
        self.button_five.pack()
        self.button_five.place(x = 80,y =120,height=40,width=50)

        self.button_six = Button(self.root,highlightthickness=0,borderwidth=0,bg = "gray10",fg = "white",text = "6",font = ("Arial",15,"bold"),command=lambda:command("6"))
        self.button_six.pack()
        self.button_six.place(x = 150,y =120,height=40,width=50)

        self.button_svn = Button(self.root,highlightthickness=0,borderwidth=0,bg = "gray10",fg = "white",text = "7",font = ("Arial",15,"bold"),command=lambda:command("7"))
        self.button_svn.pack()
        self.button_svn.place(x = 10,y =180,height=40,width=50)

        self.button_eight = Button(self.root,highlightthickness=0,borderwidth=0,bg = "gray10",fg = "white",text = "8",font = ("Arial",15,"bold"),command=lambda:command("8"))
        self.button_eight.pack()
        self.button_eight.place(x = 80,y =180,height=40,width=50)

        self.button_nine = Button(self.root,highlightthickness=0,borderwidth=0,bg = "gray10",fg = "white",text = "9",font = ("Arial",15,"bold"),command=lambda:command("9"))
        self.button_nine.pack()
        self.button_nine.place(x = 150,y =180,height=40,width=50)

        self.button_star = Button(self.root,highlightthickness=0,borderwidth=0,bg = "green",fg = "black",text = ".",font = ("Arial",17,"bold"),command=lambda:command("."))
        self.button_star.pack()
        self.button_star.place(x = 10,y =240,height=40,width=50)
        
        self.button_zero = Button(self.root,highlightthickness=0,borderwidth=0,bg = "gray10",fg = "green",text = "0",font = ("Arial",15,"bold"),command=lambda:command("0"))
        self.button_zero.pack()
        self.button_zero.place(x = 80,y =240,height=40,width=50)

        self.button_equals = Button(self.root,highlightthickness=0,borderwidth=0,bg = "yellow",fg = "black",text = "=",font = ("Arial",17,"bold"),command=main_command)
        self.button_equals.pack()
        self.button_equals.place(x = 150,y =240,height=40,width=50)
        
        self.button_delete = Button(self.root,highlightthickness=0,borderwidth=0,bg = "red",fg = "white",text = "C",font = ("Arial",20,"bold"),command = delete_object)
        self.button_delete.pack()
        self.button_delete.place(x = 220,y =60,height=40,width=50)
        
        self.button_toplama = Button(self.root,highlightthickness=0,borderwidth=0,bg = "green",fg = "white",text = "+",font = ("Arial",20,"bold"),command=lambda:command("+"))
        self.button_toplama.pack()
        self.button_toplama.place(x = 290,y =60,height=40,width=50)

        self.button_cıkartma = Button(self.root,highlightthickness=0,borderwidth=0,bg = "green",fg = "white",text = "-",font = ("Arial",20,"bold"),command=lambda:command("-"))
        self.button_cıkartma.pack()
        self.button_cıkartma.place(x = 290,y =120,height=40,width=50)

        self.button_carpma = Button(self.root,highlightthickness=0,borderwidth=0,bg = "green",fg = "white",text = "X",font = ("Arial",20,"bold"),command=lambda:command("*"))
        self.button_carpma.pack()
        self.button_carpma.place(x = 290,y =180,height=40,width=50)

        self.button_bolme = Button(self.root,highlightthickness=0,borderwidth=0,bg = "green",fg = "white",text = "/",font = ("Arial",20,"bold"),command=lambda:command("/"))
        self.button_bolme.pack()
        self.button_bolme.place(x = 290,y =240,height=40,width=50)
        
        self.button_ussu = Button(self.root,highlightthickness=0,borderwidth=0,bg = "green",fg = "white",text = "**",font = ("Arial",20,"bold"),command = lambda:command("**"))
        self.button_ussu.pack()
        self.button_ussu.place(x = 220,y =120,height=40,width=50)

        self.button_aa = Button(self.root,highlightthickness=0,borderwidth=0,bg = "green",fg = "white",text = "//",font = ("Arial",20,"bold"),command = lambda:command("//"))
        self.button_aa.pack()
        self.button_aa.place(x = 220,y =180,height=40,width=50)

        self.button_bb = Button(self.root,highlightthickness=0,borderwidth=0,bg = "green",fg = "white",text = "%",font = ("Arial",20,"bold"),command=lambda:command("%"))
        self.button_bb.pack()
        self.button_bb.place(x = 220,y =240,height=40,width=50)
        #endregion
    def Window_Loop(self):
        self.root.mainloop()

Calculator()
