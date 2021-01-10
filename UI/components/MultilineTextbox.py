from tkinter import *
from tkinter.scrolledtext import ScrolledText

class MultilineTextbox(ScrolledText):
	def __init__(self, master=None, font=None, bg=None, fg=None, x=0, y=0, **kwargs):
		super().__init__(master, font=font, bg=bg, fg=fg, **kwargs)

		self.font = font
		self.bg = bg
		self.fg = fg
		self.x = x
		self.y = y
		self.options = kwargs

		self.place(x=self.x, y=self.y)

	def getText(self, index=1.0):
		self.text = self.get(index, END)
		return self.text