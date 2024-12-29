from flask import Flask, render_template

app = Flask(__name__)

SHIT = ['ogur', 'gogus', 'cwel'] # nice list

@app.route('/')
def cwel():
  return render_template('index.html') # render templates/index.html

@app.route('/api/v1/hello') # return 'hi' lol nice api bro
def hi():
  return 'hi' # hi

@app.route('/404') # goofy ahh 404 (idk working or not)
def cwelowskagadka():
  return 'error', 404 # return 'error'

@app.route('/api/v1/cwel/shit') # nice endpoint
def list():
  return {'cwele': SHIT} # return 'SHIT' list



if __name__ == '__main__': # ok
    app.run(debug=True)
