#Creating message box after importing 'tkinter' syst. function
#firstly install tkinter using 'sudo apt-get install python3-tk'
#Now,
from tkinter import *
from tkinter import messagebox

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()

messagebox.showinfo('Message Box', 'Hello World!')

window.deiconify()
window.destroy()
window.quit()