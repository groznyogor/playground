import Flask
from Flask import render_template

app = Flask(__name__)

@app.route('/api/v1/hello')
def hi():
  return 'hi'

if __name__ == '__main__':
    app.run(debug=True)
