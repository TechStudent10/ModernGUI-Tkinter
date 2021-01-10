from tkinter import *
import tkinter as tk

class Button(tk.Button):
	def __init__(self, master=None, text="", font=None, bg=None, fg=None, x=0, y=0, command=lambda: print(""), **kwargs):
		super().__init__(master, text=text, font=font, bg=bg, fg=fg, command=command, **kwargs)

		self.text = text
		self.font = font
		self.bg = bg
		self.fg = fg
		self.x = x
		self.y = y
		self.command = command
		self.options = kwargs

		self.place(x=self.x, y=self.y)