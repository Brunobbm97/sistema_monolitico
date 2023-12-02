from flask import render_template, request, redirect
from flask import Blueprint
import conectores.conector_categoria as conector_categoria
from classes.categoria import Categoria

categorias_blueprint = Blueprint("categorias", __name__)


@categorias_blueprint.route("/categoria/mostrar")
def categorias_index():
    categoria = conector_categoria.get_all()
    return render_template("categoria/index.html", categoria = categoria, title = "Categorias_cadas")

@categorias_blueprint.route("/categoria/create",methods=['GET','POST'])
def create_categoria():
    if request.method=='GET':
        return render_template('categoria/create_categoria.html')
    
    if request.method=='POST':
        nome = request.form.get('nome')
        tipo_veiculo = request.form.get('tipo_veiculo')
        veiculo = request.form.get('veiculo')

        nova_categoria = Categoria(nome,tipo_veiculo,veiculo)
        conector_categoria.new(nova_categoria)
        return redirect("/categoria/mostrar")

@categorias_blueprint.route("/categoria/delete/<int:id>", methods=['GET','POST'])
def deleta_categoria(id):
    conector_categoria.delete_one(id)
    return redirect("/categoria/mostrar")

@categorias_blueprint.route('/categoria/update/<int:id>', methods=['GET','POST'])
def update(id):
    u = conector_categoria.get_one(id)
    if request.method=='GET':
        return render_template('categoria/update.html', u = u)
    
    if request.method=='POST':
        nome = request.form.get('nome')
        tipo_veiculo = request.form.get('tipo_veiculo')
        veiculo = request.form.get('veiculo')
        u.nome = nome
        u.tipo_veiculo = tipo_veiculo
        u.veiculo = veiculo

        nova_categoria = Categoria(u.nome, u.tipo_veiculo, u.veiculo)
        conector_categoria.update(nova_categoria, u.id)
        return redirect("/categoria/mostrar")
    