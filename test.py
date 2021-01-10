from UI import Window, Application, ExternalWindow
from UI.components import Text, Textbox, Button, MultilineTextbox

app = Application()
window = Window((350, 200))

app.root = window

def login(username, password):
	app2 = Application()
	window2 = ExternalWindow(master=app2, widthHeight=(350, 200))

	app2.root = window2

	textbox = MultilineTextbox(**{
		"x": 0,
		"y": 0,
		"border": 0,
		"master": app2
	})

	app.run()

usernText = Text(**{
	"text": "Username: ",
	"x": 50,
	"y": 50
})

username = Textbox(**{
	"x": 150,
	"y": 50
})


passwText = Text(**{
	"text": "Password: ",
	"x": 50,
	"y": 100
})

password = Textbox(**{
	"x": 150,
	"y": 100,
	"secret": True
})

loginButton = Button(**{
	"x": 100,
	"y": 150,
	"text": "Login",
	"command": lambda: login(username.getText(), password.getText())
})

app.run()