from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('playground_index.html')

@app.route('/success')
def success():
    return "Success"

if __name__=="__main__":
    app.run(debug=True,)

