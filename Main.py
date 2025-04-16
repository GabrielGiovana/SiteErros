from flask import Flask, render_template, request, redirect, url_for
import Bd
import Bd_Classes

app = Flask(__name__)

@app.route("/")
def home():
    lista_de_problemas = Bd.problema()
    return render_template("index.html", problemas=lista_de_problemas) 

# @app.route("/cadastrar", methods=["GET", "POST"])
# def novo_problema():
#     if request.method == "POST":
#         titulo = request.form["titulo"]
#         descricao = request.form["descricao"]
#         solucao = request.form["solucao"]
#         evitar = request.form["evitar"]
#         imagem = request.form["imagem"]
#         tag = request.form["tag"]

#         problema = Bd_Classes.Problema(titulo, descricao, solucao, evitar, imagem, tag)
#         Bd.inserirProblema(problema)

#         return render_template("teste.html")
    
#     elif request.method == "GET":
#       return render_template("teste.html")




if __name__ == "__main__":
    app.run(debug=True)



