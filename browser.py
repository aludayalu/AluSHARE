from tkinter import *
from tkhtmlview import HTMLLabel
def start(htm):
	root = Tk()
	root.geometry("400x400")
	my_label = HTMLLabel(root,html=htm)
	my_label.pack()
	root.attributes('-topmost',True)
	root.title('Lumatozer')
	root.mainloop()