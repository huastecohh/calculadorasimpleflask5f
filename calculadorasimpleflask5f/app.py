from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'sumar':
                result = num1 + num2
            elif operation == 'restar':
                result = num1 - num2
            elif operation == 'multiplicar':
                result = num1 * num2
            elif operation == 'dividir':
                if num2 != 0:
                    result = num1 / num2
                else:
                    error = "Error: Division por cero no permitida."
        except ValueError:
            error = "Error: Por favor ingrese numeros validos."

    return render_template('index.html', result=result, error=error)




if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
