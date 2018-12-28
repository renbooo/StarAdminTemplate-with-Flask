from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/textretrieve', methods=['GET'])
def textretrieve():
  return render_template('textretrieve.html')

@app.route('/imageretrieve', methods=['GET'])
def imageretrieve():
  return render_template('imageretrieve.html')

@app.route('/textimageretrieve', methods=['GET'])
def textimageretrieve():
  return render_template('textimageretrieve.html')

if __name__ == '__main__':
  app.run(debug=True)