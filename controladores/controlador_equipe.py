from flask import render_template, request, redirect
from flask import Blueprint
import conectores.conector_equipe as conector_equipe
from classes.equipe import Equipe

equipes_blueprint = Blueprint("equipe", __name__)


@equipes_blueprint.route("/equipe/mostrar")
def equipe_index():
    equipe = conector_equipe.get_all()
    return render_template("/equipe/index.html", equipe = equipe, title = "equipes_cadas")

@equipes_blueprint.route("/equipe/create",methods=['GET','POST'])
def equipe_equipe():
    if request.method=='GET':
        return render_template('/equipe/create_equipe.html')
    
    if request.method=='POST':
        nome = request.form.get('nome')
        tipo_veiculo = request.form.get('tipo_veiculo')
        veiculo = request.form.get('veiculo')

        nova_equipe = Equipe(nome,tipo_veiculo,veiculo)
        conector_equipe.new(nova_equipe)
        return redirect("/equipe/mostrar")

@equipes_blueprint.route("/equipe/delete/<int:id>", methods=['GET','POST'])
def deleta_equipe(id):
    conector_equipe.delete_one(id)
    return redirect("/equipe/mostrar")

@equipes_blueprint.route("/equipe/update/<int:id>", methods=['GET','POST'])
def update_equipe(id):
    u = conector_equipe.get_one(id)
    if request.method=='GET':
        return render_template('/equipe/update_equipe.html', u = u)
    
    if request.method=='POST':
        nome = request.form.get('nome')
        tipo_veiculo = request.form.get('tipo_veiculo')
        veiculo = request.form.get('veiculo')
        u.nome = nome
        u.tipo_veiculo = tipo_veiculo
        u.veiculo = veiculo

        nova_equipe = Equipe(u.nome, u.tipo_veiculo, u.veiculo)
        conector_equipe.update(nova_equipe, u.id)
        return redirect("/equipe/mostrar")
    