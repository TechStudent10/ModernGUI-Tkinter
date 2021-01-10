from tkinter import *

class Text(Label):
	def __init__(self, master=None, text="", font=None, bg=None, fg=None, x=0, y=0, **kwargs):
		super().__init__(master, text=text, font=font, bg=bg, fg=fg, **kwargs)

		self.text = text
		self.font = font
		self.bg = bg
		self.fg = fg
		self.x = x
		self.y = y
		self.options = kwargs

		self.place(x=self.x, y=self.y)