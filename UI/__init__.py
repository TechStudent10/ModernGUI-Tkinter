try:
	from Tkinter import *
except ImportError:
	from tkinter import *

if __name__ == "__main__":
	from errors import *
else:
	from .errors import *

import os, sys, zlib, base64

icon=zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

class Window(Frame):
	def __init__(self, widthHeight=(640, 480), **kw):
		super().__init__(None, **kw)

		self.width, self.height = widthHeight[0], widthHeight[1]
		self.configure(width=self.width, height=self.height)

class ExternalWindow(Frame):
	def __init__(self, master=None, widthHeight=(640, 480), **kw):
		super().__init__(master=master, **kw)
		self.master = master

		self.width, self.height = widthHeight[0], widthHeight[1]
		self.configure(width=self.width, height=self.height)


class Application(Tk):
	def __init__(self, windowType=None):
		super().__init__()

		self.root = windowType
		self.title = "Application"
		self.iconbitmap(icon)

	def run(self, n=0):
		if self.root is not None:
			self.root.pack(fill=BOTH, expand=1)
		else:
			raise WindowNotFound()

		super().title(self.title)
		self.mainloop(n)