from flask import Flask, render_template, request, redirect, url_for
import Bd
import Bd_Classes

app = Flask(__name__)

@app.route("/")
def home():
    lista_de_problemas = Bd.problema()
    return render_template("index.html", problemas=lista_de_problemas)

@app.route("/cadastrar", methods=["POST"])
def novo_problema():
    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        solucao = request.form["solucao"]
        evitar = request.form["evitar"]
        tag = request.form["tag"]

        problema = Bd_Classes.Problema(titulo, descricao, solucao, evitar,tag)
        Bd.inserirProblema(problema)

        return redirect("/")


@app.route('/problema/<int:id>')
def detalhes_problema(id):
    problema = Bd.get_problema_by_id(id)
    if problema:
        return render_template('detalhes.html', problema=problema)
    


if __name__ == "__main__":
    app.run(debug=True)