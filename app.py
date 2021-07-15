import tkinter as tk
from functools import partial  

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def copy_to_clipboard(self, text):
        print("copy")
        clipb = tk.Tk()
        clipb.withdraw()
        clipb.clipboard_clear()
        clipb.clipboard_append(text.get())
        clipb.update() # now it stays on the clipboard after the window is closed
        clipb.destroy()

    def create_widgets(self):
        tk.Label(self, text="Set text").grid(row=0)

        data_clip = tk.StringVar()

        text1 = tk.Entry(self, textvariable=data_clip)

        copy_to_clipboard = partial(self.copy_to_clipboard, data_clip) #now copy_to_clipboard has 2 arguments
        
        btn_copy = tk.Button(
            self,
            text="copy",
            command=copy_to_clipboard
        )

        text1.grid(row=0, column=1)
        btn_copy.grid(row=0, column=2)
    

root = tk.Tk()
app = Application(master=root)
app.mainloop()