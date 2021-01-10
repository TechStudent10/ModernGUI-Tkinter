from UI import Window, Application
from UI.components import Text

class MainApp(Application):
	def __init__(self):
		super().__init__()
		self.window = Window((640, 480))
		self.root = self.window

		self.text = Text(**{
			"x": 50,
			"y": 50,
			"text": "Hello World!"
		})

if __name__ == '__main__':
	app = MainApp()
	app.title = "Main App"
	app.run()