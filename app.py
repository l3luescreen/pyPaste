import tkinter as tk
import clipboard
import pyperclip
import os

from functools import partial
from tkinter.filedialog import askopenfilename 

#global variable
clip_Text = ""
state = "show"

#global function
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # variable
        global clip_Text
        clip_Text = tk.StringVar()

        item_text = tk.Label(self, text="Set text")
        text1 = tk.Entry(self, textvariable = clip_Text)
        btn_copy = tk.Button(self, text="copy", command=self.copy_to_clipboard)
        btn_paste = tk.Button(self, text="paste", command=self.paste_text)

        item_text.grid(row=0, column=0)
        text1.grid(row=0, column=1)
        btn_copy.grid(row=0, column=2)
        btn_paste.grid(row=0, column=3)
        self.pack()
    
    def copy_to_clipboard(e, self=None):
        global clip_Text
        data = '\033[1m' + clip_Text.get() + '\033[0m'
        clipboard.copy(data)
        print('Copied to clipboard: ' + data)

    def paste_text(e, self=None):
        print('Paste text :' + clipboard.paste())
        pyperclip.paste()
    
    def hide_show(e, self=None):
        global state
        if state == 'show':
            state = 'hide'
            root.withdraw()
        elif state == 'hide':
            state = 'show'
            root.deiconify()

root = tk.Tk()
root.title("pyPaste")
app = Application(master=root)

# set root bind
root.bind("<Tab>", app.hide_show)
root.bind("<Shift_L>", app.copy_to_clipboard)
root.bind("<Return>", app.paste_text)

app.mainloop()
