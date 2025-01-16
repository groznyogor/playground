from flask import Flask, render_template, jsonify
from datetime import datetime
import random

# welcome to the most brainrot flask app on earth
# me coding at 3AM: "yes this is genius"
# flask brainrot by groznyogor industries

app = Flask(__name__)

SHIT = ['ogur', 'brainrotpy']
KAJA_GODEK = ['krzysiu', 'to', 'jebany', 'debil', 'co', 'sra', 'na', 'paste']

@app.route('/')
def home():
    # "render_template is temporary, chaos is forever"
    return render_template('index.html') # chaos edition

@app.route('/api/v1/hello')
def hi():
    return 'siemano cwelu' # no more boring "hi"

@app.route('/404') # certified hood classic 404
def error_404():
    return 'chuja dziala, dziwi cie to?', 404

@app.route('/api/v1/cwel/shit')
def list_shit():
    return {'cwele': SHIT, 'count': len(SHIT)} # now with a count!!

@app.route('/api/v1/hour')
def godzina_gigachada():
    current_time = datetime.now()
    current_hour = current_time.hour
    current_minute = current_time.minute
    return f'lape godzine: {current_hour}:{current_minute} (skurwysynie lap tajma)'

@app.route('/api/v1/say/<text>') 
def mowi(text):
    reversed_text = text[::-1] # mowi ale na odwrot
    processed_text = text.upper() 
    return jsonify({
        "original": text,
        "processed": processed_text,
        "reversed": reversed_text
    })

@app.route('/api/v1/kajagodek/wymordowac')
def ultimate_message():
    random_insult = random.choice(KAJA_GODEK)
    return f'witaj, twoja losowa wiadomosc: "{random_insult}"'

@app.route('/api/v1/random/shit') # fun endpoint
def random_shit():
    random_item = random.choice(SHIT)
    return f'twoje losowe gowno to: {random_item}'

@app.route('/api/v1/coinflip') # now gambling is here
def coin_flip():
    result = random.choice(['orzel', 'reszka'])
    return f'wynik rzutu moneta: {result} (kto przegral - cwel)'

@app.route('/api/v1/counter/<int:number>')
def licznik(number):
    if number < 0:
        return f'liczby ujemne? co to za bieda: {number}', 400
    return jsonify({
        "original": number,
        "squared": number ** 2,
        "cubed": number ** 3
    })

if __name__ == '__main__':
    app.run(debug=True)
