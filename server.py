from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<color>/<int:x>') 

def index(color = 'blue',x=3):
    return render_template('playground_index.html',x=x, color=color)

@app.route('/success')
def success():
    return "Success"


if __name__=="__main__":
    app.run(debug=True)

