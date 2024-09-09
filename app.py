from flask import Flask, render_template, request

#Esse é nome do site
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/submit', methods=['POST'])
def submit():

    tipo = request.form.get('tipo')
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    peso = request.form.get('peso')

    try:
        idade = int(idade)
        if idade < 0:
            return "A idade não pode ser negativa.", 400
    except ValueError:
        return "Por favor, insira um número válido para a idade.", 400

    try:
        peso = float(peso)
        if peso < 0:
            return "O peso não pode ser negativo.", 400
    except ValueError:
        return "Por favor, insira um número válido para o peso.", 400

    return render_template("result.html", tipo=tipo, nome=nome, idade=idade, peso=peso) 

if __name__ == '__main__':
    app.run(debug=True)