from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def index():
    return 'é o programação na prática'

@app.route('/sobremim')
def sobremim():
    return render_template('sobreMim.html')

@app.route('/projetos')
def projetos():
    return render_template('trabalhos.html')

if __name__ == '__main__':
    app.run()
