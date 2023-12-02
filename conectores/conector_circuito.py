from database.run_sql import run_sql
from classes.circuito import Circuito

def get_all():

    circuito = []

    sql = "SELECT * FROM public.tb_circuito ORDER BY id ASC "
    results = run_sql(sql)

    for row in results:
        agendamento = Circuito(row["nome_circuito"], 
                               row["distancia_volta"], 
                               row["pais"], 
                               row["num_voltas"], 
                               row["categoria"], 
                               row["id"])
        circuito.append(agendamento)

    return circuito

def new(circuito):

    sql = "INSERT INTO public.tb_circuito ( nome_circuito, distancia_volta, pais, num_voltas, categoria  ) VALUES ( %s, %s, %s);"
    values = [ circuito.nome_circuito, circuito.distancia_volta, circuito.pais,circuito.num_voltas, circuito.categoria  ]

    run_sql(sql, values)

    return circuito

def delete_one(id):
    sql = "DELETE FROM public.tb_circuito WHERE id = %s"
    value = [id]
    run_sql(sql, value)

def update(circuito, id):
    sql = "UPDATE public.tb_circuito SET  nome_circuito = %s ,distancia_volta = %s, pais, num_voltas = %s, categoria = %s WHERE id = %s"
    value = [ circuito.nome_circuito, circuito.distancia_volta, circuito.pais,circuito.num_voltas, circuito.categoria, id ]

    run_sql(sql,value)

######
def get_one(id):

    sql = "SELECT * FROM public.tb_circuito WHERE id = %s"
    value = [id]

    result = run_sql(sql, value)[0]

    circuito = Circuito(result["nome"], result["tipo_veiculo"], result["veiculo"], result["id"])

    return circuito