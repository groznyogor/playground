from flask import Flask, render_template
from datetime import datetime

# hello hello hello, im VIP MTW texas patrick sigma, skibidi
# soon brainrot pyton
# flask so bad!!!

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

@app.route('/api/v1/hour') # hour endpoint (system clock doesnt exist)
def dawajgodzinepedale():
    current_time = datetime.now()
    current_hour = current_time.hour
    return f'lap godzine skurwysynie: {current_hour}' # take hour sweetie



if __name__ == '__main__': # ok
    app.run(debug=True) # debuk ebok
