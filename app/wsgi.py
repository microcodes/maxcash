from . import create_app


app = create_app('development')
app.app_context().push()

if __name__ == '__main__':
	app.run()