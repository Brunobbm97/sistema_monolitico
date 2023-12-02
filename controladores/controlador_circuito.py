from flask import render_template, request, redirect
from flask import Blueprint
import conectores.conector_circuito as conector_circuito
from classes.circuito import Circuito

circuitos_blueprint = Blueprint("circuito", __name__)


@circuitos_blueprint.route("/circuito/mostrar")
def circuito_index():
    circuito = conector_circuito.get_all()
    return render_template("/circuito/index.html", circuito = circuito, title = "circuitos_cadas")

@circuitos_blueprint.route("/circuito/create",methods=['GET','POST'])
def circuito_circuito():
    if request.method=='GET':
        return render_template('circuito/create_circuito.html')
    
    if request.method=='POST':
        nome_circuito = request.form.get('nome')
        distancia_volta = request.form.get('distancia_volta')
        pais = request.form.get('pais')
        num_voltas = request.form.get('num_voltas')
        categoria = request.form.get('categoria')

        nova_circuito = Circuito(nome_circuito,distancia_volta,pais,num_voltas,categoria)
        conector_circuito.new(nova_circuito)
        return redirect("/circuito/mostrar")

@circuitos_blueprint.route("/circuito/delete/<int:id>", methods=['GET','POST'])
def deleta_circuito(id):
    conector_circuito.delete_one(id)
    return redirect("/circuito/mostrar")

@circuitos_blueprint.route("/circuito/update/<int:id>", methods=['GET','POST'])
def update_circuito(id):
    u = conector_circuito.get_one(id)
    if request.method=='GET':
        return render_template('/circuito/update_circuito.html', u = u)
    
    if request.method=='POST':
        nome = request.form.get('nome')
        tipo_veiculo = request.form.get('tipo_veiculo')
        veiculo = request.form.get('veiculo')
        u.nome = nome
        u.tipo_veiculo = tipo_veiculo
        u.veiculo = veiculo

        nova_circuito = Circuito(u.nome, u.tipo_veiculo, u.veiculo)
        conector_circuito.update(nova_circuito, u.id)
        return redirect("/circuito/mostrar")
    