class WindowNotFound(Exception):
	def __init__(self, window):
		super().__init__("Window '" + str(window) + "' not found.")