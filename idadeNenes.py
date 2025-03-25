from datetime import date, datetime

def calcular_idade(data_nascimento):
    hoje = date.today()
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%y").date()
    
    anos = hoje.year - nascimento.year
    meses = hoje.month - nascimento.month
    dias = hoje.day - nascimento.day

    if dias < 0:
        meses -= 1
        dias += (hoje.replace(day=1) - hoje.replace(month=hoje.month-1, day=1)).days

    if meses < 0:
        anos -= 1
        meses += 12

    return anos, meses, dias

nenes = {
    "Alaska": "15/09/16",
    "Pandora": "20/11/18",
    "Píppin": "26/12/24"
}

for nome, data_nascimento in nenes.items():
    anos, meses, dias = calcular_idade(data_nascimento)
    print(f"{nome} tem {anos} anos, {meses} meses e {dias} dias.")

