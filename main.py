import Flask
from Flask import render_template

app = Flask(__name__)

@app.route('/')
def cwel():
  return render_template('index.html') # render templates/index.html

@app.route('/api/v1/hello') # return 'hi' lol nice api bro
def hi():
  return 'hi' # hi

@app.route('/404') # goofy ahh 404 (idk working or not)
def cwelowskagadka():
  return 'error' # return 'error'

if __name__ == '__main__': # ok
    app.run(debug=True)
