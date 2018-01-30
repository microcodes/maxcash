from app import app, r

@app.route('/')
@app.route('/index')
def index():

	return r.lpop('Ali')