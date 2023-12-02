from database.run_sql import run_sql
from classes.equipe import Equipe

def get_all():

    equipe = []

    sql = "SELECT * FROM public.tb_equipe ORDER BY id ASC "
    results = run_sql(sql)

    for row in results:
        agendamento = Equipe(row["nome"], row["tipo_veiculo"], row["veiculo"], row["id"])
        equipe.append(agendamento)

    return equipe

def new(equipe):

    sql = "INSERT INTO public.tb_equipe ( nome_equipe, distancia_volta, pais, num_voltas, categoria  ) VALUES ( %s, %s, %s);"
    values = [ equipe.nome, equipe.tipo_veiculo, equipe.veiculo ]

    results = run_sql(sql, values)

    return equipe

def delete_one(id):
    sql = "DELETE FROM public.tb_equipe WHERE id = %s"
    value = [id]
    run_sql(sql, value)

def update(equipe, id):
    sql = "UPDATE public.tb_equipe SET  nome_equipe = %s ,distancia_volta = %s, pais, num_voltas = %s, categoria = %s WHERE id = %s"
    value = [ equipe.nome, equipe.tipo_veiculo, equipe.veiculo, id ]

    run_sql(sql,value)

######
def get_one(id):

    sql = "SELECT * FROM public.tb_equipe WHERE id = %s"
    value = [id]

    result = run_sql(sql, value)[0]

    equipe = Equipe(result["nome"], result["tipo_veiculo"], result["veiculo"], result["id"])

    return equipe