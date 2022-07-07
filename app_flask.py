import pandas as pd
from flask import render_template, Flask


class Cria_Acesso():
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha= senha


usuario = Cria_Acesso("Rafael","1234")


class Portfolio():
    pass


app = Flask(__name__)


@app.route('/')
def login():
    return render_template("login.html")


app.run(debug=True)
