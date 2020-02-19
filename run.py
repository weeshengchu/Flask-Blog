from flaskblog import app

# allow us to run 'python flaskblog.py' instead of 'flask run'
if __name__ == '__main__':
    app.run(debug=True)
