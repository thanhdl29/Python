from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)
        
        Style().configure("TFrame", background="#333")
        
        bard = Image.open("D:\\Pictures\\Camera Roll\\1.jpg")
        bard = bard.resize((100, 100), Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)
        
        bard = Image.open("D:\\Pictures\\Camera Roll\\1.jpg")
        bard = bard.resize((100, 100), Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=40, y=160)
        
        bard = Image.open("D:\\Pictures\\Camera Roll\\1.jpg")
        bard = bard.resize((100, 100), Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=170, y=50)
        
        
        
       
        

root = Tk()
root.geometry("800x600")
app = Example(root)
root.mainloop()