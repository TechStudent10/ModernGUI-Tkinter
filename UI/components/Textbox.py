from tkinter import *

class Textbox(Entry):
	def __init__(self, master=None, font=None, bg=None, fg=None, x=0, y=0, secret=False, **kwargs):
		super().__init__(master, font=font, bg=bg, fg=fg, **kwargs)

		self.font = font
		self.bg = bg
		self.fg = fg
		self.x = x
		self.y = y
		self.secret = secret
		self.var = StringVar()
		self.options = kwargs

		if self.secret:
			self.config(show="*")

		self.config(textvariable=self.var)
		self.place(x=self.x, y=self.y)

	def getText(self):
		self.text = self.get()
		return self.text