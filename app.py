from flask import Flask, render_template, request

app = Flask(__name__)

def sumar(a, b):
    return a + b

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None
    if request.method == 'POST':
        try:
            val1 = float(request.form['val1'])
            val2 = float(request.form['val2'])
            resultado = sumar(val1, val2)
        except ValueError:
            resultado = "Error: Ingresa números válidos"
    return render_template('index.html', resultado=resultado)

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)