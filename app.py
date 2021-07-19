import tkinter as tk
import clipboard

from functools import partial
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # variable
        self.data_clip = tk.StringVar()

        item_text = tk.Label(self, text="Set text")

        text1 = tk.Entry(self, textvariable = self.data_clip)

        
        copy_to_clipboard = partial(self.copy_to_clipboard, self.data_clip) #now copy_to_clipboard has 2 arguments
        btn_copy = tk.Button(self, text="copy", command=copy_to_clipboard)
        btn_paste = tk.Button(self, text="paste", command=self.paste_text)


        # btn_copy.bind("<Enter>", self.copy_to_clipboard(self.data_clip))

        item_text.grid(row=0, column=0)
        text1.grid(row=0, column=1)
        btn_copy.grid(row=0, column=2)
        btn_paste.grid(row=0, column=3)
    
    def copy_to_clipboard(self, text):
        data = text.get()
        clipboard.copy(data)

    def paste_text(self):
        print(clipboard.paste())
  

root = tk.Tk()
root.title("pyPaste")
app = Application(master=root)
app.mainloop()