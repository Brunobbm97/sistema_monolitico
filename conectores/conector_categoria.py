from database.run_sql import run_sql
from classes.categoria import Categoria

def get_all():

    categoria = []

    sql = "SELECT * FROM public.tb_categoria ORDER BY id ASC "
    results = run_sql(sql)

    for row in results:
        agendamento = Categoria(row["nome"], row["tipo_veiculo"], row["veiculo"], row["id"])
        categoria.append(agendamento)

    return categoria

def new(categoria):

    sql = "INSERT INTO public.tb_categoria ( nome, tipo_veiculo, veiculo ) VALUES ( %s, %s, %s);"
    values = [ categoria.nome, categoria.tipo_veiculo, categoria.veiculo ]

    results = run_sql(sql, values)

    return categoria

def delete_one(id):
    sql = "DELETE FROM public.tb_categoria WHERE id = %s"
    value = [id]
    run_sql(sql, value)

def update(categoria, id):
    sql = "UPDATE public.tb_categoria SET nome = %s, tipo_veiculo = %s, veiculo = %s WHERE id = %s"
    value = [ categoria.nome, categoria.tipo_veiculo, categoria.veiculo, id ]

    run_sql(sql,value)

######
def get_one(id):

    sql = "SELECT * FROM public.tb_categoria WHERE id = %s"
    value = [id]

    result = run_sql(sql, value)[0]

    categoria = Categoria(result["nome"], result["tipo_veiculo"], result["veiculo"], result["id"])

    return categoria