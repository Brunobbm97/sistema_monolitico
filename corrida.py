from flask import Flask, render_template
from controladores.controlador_categoria import categorias_blueprint
from controladores.controlador_circuito import circuitos_blueprint
from controladores.controlador_equipe import equipes_blueprint

app = Flask(__name__)

app.register_blueprint(categorias_blueprint)
app.register_blueprint(circuitos_blueprint)
app.register_blueprint(equipes_blueprint)

@app.route("/")
def home():
    return render_template('index.html')

# Executa
if __name__ == "__main__":
    app.run(debug = True)